# Calibration Certificate Key Extractor Chatbot

## Description
This project creates a chatbot that can extract key components from calibration certificates. The application is easy to use and is packaged in a Docker Compose format with two services: the actual application and a Neo4j database image pulled from Docker Hub.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

### Prerequisites
- Ensure you have [Docker](https://www.docker.com/get-started) installed on your machine.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/calibration-certificate-chatbot.git
   
2. Create a .env file in the same directory as the docker-compose.yml file and add the following environment variables with your credentials:
   ```sh
   # Set these Environment Variables (required by embedding)
   AZURE_OPENAI_API_KEY=
   AZURE_OPENAI_ENDPOINT=
   
   # Set Environment Variables for GPT 3.5 Turbo
   OPENAI_API_KEY_3=
   DEPLOYMENT_NAME_LLM_3=
   DEPLOYMENT_NAME_EMBED_3=
   OPENAI_API_TYPE_3=
   OPENAI_API_VERSION_3=
   AZURE_OPENAI_ENDPOINT_3=
   
   # Set Environment Variables for GPT 4
   OPENAI_API_KEY_4=
   DEPLOYMENT_NAME_LLM_4=
   DEPLOYMENT_NAME_EMBED_4=
   OPENAI_API_TYPE_4=
   OPENAI_API_VERSION_4=
   AZURE_OPENAI_ENDPOINT_4=

3. Ensure the .env file is saved in the same directory as docker-compose.yml.

4. Start the application by running the following command:
   ```sh
   docker compose up
## Usage
1. After running docker compose up, the application will start and connect to the Neo4j database.
2. The chatbot will be available at http://localhost:8080.
3. The Neo4j database can be accessed at http://localhost:7474. You can view the database with a simple command like:
   ```sh
   MATCH (n) RETURN (n) on Neo4j Application;

