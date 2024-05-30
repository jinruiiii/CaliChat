# import libraries
import chainlit as cl
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_community.document_loaders import UnstructuredFileLoader
from filetype import guess
import httpx
from langchain_openai import AzureOpenAIEmbeddings
import ssl
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.vectorstores import Neo4jVector
from langchain_community.graphs import Neo4jGraph
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains.llm import LLMChain
import prompt_templates as pt
from langchain.vectorstores.neo4j_vector import Neo4jVector
import time
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import requests

os.environ['CURL_CA_BUNDLE'] = ''
os.environ["AZURE_OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY_EMBEDDING"]
os.environ["AZURE_OPENAI_ENDPOINT"] = os.environ["OPENAI_ENDPOINT_EMBEDDING"]

# initialise gpt4
azure_configs_gpt4 ={      
    "azure_endpoint" : os.environ["OPENAI_ENDPOINT"],
    "openai_api_version" : os.environ["OPENAI_API_VERSION"],
    "azure_deployment" : os.environ["OPENAI_DEPLOYMENT_NAME"],
    "openai_api_key" : os.environ["OPENAI_API_KEY"],
    "openai_api_type" :os.environ["OPENAI_API_TYPE"],
    "http_client": httpx.Client(verify=False),
}
llm_4 = AzureChatOpenAI(**azure_configs_gpt4)

# initialise neo4j graph
graph = Neo4jGraph(
    url="bolt://neo4j:7687", username="neo4j", password="pleaseletmein"
)

# initialise ada-002 embedding
httpx_client = httpx.Client(http2=True, verify=False)
embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.environ["OPENAI_DEPLOYMENT_NAME_EMBEDDING"],
    openai_api_version = os.environ["OPENAI_API_VERSION_EMBEDDING"],
    http_client=httpx_client
)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=8000, chunk_overlap=0, length_function=len)

welcome_message = """Welcome to the DSOPdfBot! To get started:
1. Upload a PDF file.
2. Ask questions about the file!
"""


# function detects the type of document and return the document type
def detect_document_type(document_path):
    guess_file = guess(document_path)
    file_type = ""
    image_types = ['jpg', 'jpeg', 'png', 'gif']
    if(guess_file.extension.lower() == "pdf"):
        file_type = "pdf"
    elif(guess_file.extension.lower() in image_types):
        file_type = "image"
    else:
        file_type = "unknown"
    return file_type

# function extract the content of pdf file using UnstructuredFileLoader (pytesseract)
def extract_file_content(file_path):
    file_type = detect_document_type(file_path)
    if(file_type == "pdf"):
        loader = UnstructuredFileLoader(file_path, mode="elements")
    documents = loader.load()
    documents_content = '\n'.join(doc.page_content for doc in documents)
    return documents_content

# wrapper function that calls extract_file_content
def get_content(file):
    fname = file.path
    content = extract_file_content(fname)
    return content

# user question will be passed to this function during retrieval stage
def chat_interaction(query):
    global contextualized_vectorstore_forward
    global contextualized_vectorstore_backward
    global qa_forward
    global qa_backward
    try:
        contextualized_vectorstore_forward.similarity_search(query, k=1)[0].page_content
        response = qa_forward.invoke({'question': query})["answer"]
    except IndexError:
        try: 
            contextualized_vectorstore_backward.similarity_search(query, k=1)[0].page_content
            response = qa_backward.invoke({'question': query})["answer"]
        except IndexError:
            response = "There is nothing related to your query in the database"
    return response

# function to choose which retrieval methods on a vector databse. not in use with current gpt4 implementation
def select_retriever(db, name, llm):
    options = ["base", "multi", "compress"]
    base_retriever = db.as_retriever()
    if name not in options:
        print("Invalid retrever name")
        return -1
    elif name == "base":
        return base_retriever
    elif name == "multi":
        multi_retriever = MultiQueryRetriever.from_llm(
            retriever = db.as_retriever(), llm=llm
        )
        return multi_retriever
    else:
        compressor = LLMChainExtractor.from_llm(llm)
        compression_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=db.as_retriever(k=7))
        return compression_retriever
    
       
key_components_prompt = ChatPromptTemplate.from_messages([ ("system", f'''{pt.system_message_key_components_prompt}'''), ("human", "{user_input}"),])   
basic_check_prompt = ChatPromptTemplate.from_messages([ ("system", f'''{pt.system_basic_check_prompt}'''), ("human", "{user_input}"),])
entity_prompt = ChatPromptTemplate.from_messages([ ("system", f'''{pt.system_message_entity_prompt}'''), ("human", "{user_input}"),])  
cypher_prompt = ChatPromptTemplate.from_messages([ ("system", f'''{pt.system_message_cypher_prompt}'''), ("human", "{user_input}"),])  

key_components_chain = LLMChain(llm=llm_4, prompt=key_components_prompt)
basic_check_chain = LLMChain(llm=llm_4, prompt=basic_check_prompt)
entity_chain = LLMChain(llm=llm_4, prompt=entity_prompt)
cypher_chain = LLMChain(llm=llm_4, prompt=cypher_prompt)

memory = ConversationBufferWindowMemory(memory_key='chat_history', return_messages=True, output_key="answer", k=3)

contextualized_vectorstore_forward = None
contextualized_vectorstore_backward = None

qa_forward = None
qa_backward = None

chat_history = []


def get_key_components(content):
    key_components = key_components_chain.run(content)
    return key_components

def get_entities_and_rs(key_components):
    entities_and_rs = entity_chain.run(key_components)
    return entities_and_rs

def get_cypher(entities_and_rs):
    cypher = cypher_chain.run(entities_and_rs)
    return cypher


@cl.author_rename
def rename(orig_author: str):
    rename_dict = {"Chatbot": "DSOPdfBot"}
    return rename_dict.get(orig_author, orig_author)

@cl.on_chat_start
async def on_chat_start():
    
    global contextualized_vectorstore_forward
    global contextualized_vectorstore_backward
    global qa_forward
    global qa_backward

    # clean the database
    graph.query(
            """
            MATCH(n)
            DETACH DELETE n
        """
        )
    files = None
    
    # wait for user input
    while files is None:
        files = await cl.AskFileMessage(
            content=welcome_message,
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=540,
        ).send()
    file = files[0]
    print(files)
    msg = cl.Message(content=f"Processing '{file.name}'......", disable_feedback=True)
    await msg.send()
    await msg.update()


    start = time.time()
    # ocr with pytesseract
    content = await cl.make_async(get_content)(file)

    # retrieve key components
    key_components = await cl.make_async(get_key_components)(content)
    print(key_components)

    # retrieve entities and relationships
    entities_and_rs = await cl.make_async(get_entities_and_rs)(key_components)
    print(entities_and_rs)

    # generate the cypher query to populate the graph
    cypher = await cl.make_async(get_cypher)(entities_and_rs)
    print(cypher)
    try:
        graph.query(cypher)
    except:
        print("--------------------------------------")
        print("-----------ERROR WHEN QUERY-----------")
        print("--------------------------------------")
        convo_chain_out = "Sorry, your document does not contain any information that can be extracted"
    
    # update the graph database
    graph.refresh_schema()
    end = time.time()
    print(f"Ingestion Time: {end-start}")

    # embed the nodes in Neo4j graph
    vector_index = Neo4jVector.from_existing_graph(
        embeddings,
        url = "bolt://neo4j:7687",
        username="neo4j",
        password="pleaseletmein",
        index_name="calibration_index",
        node_label="Device",
        text_node_properties=["modelNumber", "name", "serialNumber", "type"],
        embedding_node_property="embedding"
    )
    print("------------Line after creating vector index------------")
    # injecting contextualized query
    contextualized_vectorstore_forward = Neo4jVector.from_existing_index(
        embeddings,
        url = "bolt://neo4j:7687",
        username="neo4j",
        password="pleaseletmein",
        index_name="calibration_index",
        retrieval_query=pt.contextualized_query_forward
    )

    contextualized_vectorstore_backward = Neo4jVector.from_existing_index(
        embeddings,
        url = "bolt://neo4j:7687",
        username="neo4j",
        password="pleaseletmein",
        index_name="calibration_index",
        retrieval_query=pt.contextualized_query_backward
    )
    print("------------Line after creating contextualized query------------")
    qa_forward = ConversationalRetrievalChain.from_llm(
        llm=llm_4,
        retriever=contextualized_vectorstore_forward.as_retriever(k=1), 
        return_source_documents=True,
        memory=memory
    )

    qa_backward = ConversationalRetrievalChain.from_llm(
        llm=llm_4,
        retriever=contextualized_vectorstore_backward.as_retriever(k=1), 
        return_source_documents=True,
        memory=memory
    )
    print("------------Line after creating retrieval chain------------")
    msg.content = f"'{file.name}' has been processed.\n\n\n {basic_check_chain.run(key_components)} \n\n\n ---------- Below is a summary of the certificate ----------\n {key_components}" 
    await msg.update()

@cl.on_message
async def main(message: cl.Message):
    query = message.content
    print(query)
    response = await cl.make_async(chat_interaction)(query)
    await cl.Message(
        response,
    ).send()