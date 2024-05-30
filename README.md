# PCB Object Detection

## Description
This project is an application designed to process PCB (Printed Circuit Board) images. By uploading PCB images to the application, the application can detect individual components and read text labels such as "R1" and "R2" on the PCB. The application is user-friendly and leverages advanced machine learning and OCR (Optical Character Recognition) techniques to provide results.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

### Prerequisites
- Ensure you have the following dependencies.
  1. dfasdfd
  2. 2dsfsdafdas
  3. 

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/calibration-certificate-chatbot.git
   
2. Create a .env file in the same directory as the docker-compose.yml file and add the following environment variables with your credentials:
   ```sh
   # Set Environment Variables for Chatbot Backbone Model
   OPENAI_API_KEY= 
   OPENAI_API_VERSION=
   OPENAI_API_TYPE= 
   OPENAI_ENDPOINT= 
   OPENAI_DEPLOYMENT_NAME= 
   
   # Set Environment Variables for Embedding Model
   OPENAI_API_KEY_EMBEDDING=
   OPENAI_API_VERSION_EMBEDDING= 
   OPENAI_API_TYPE_EMBEDDING= 
   OPENAI_ENDPOINT_EMBEDDING= 
   OPENAI_DEPLOYMENT_NAME_EMBEDDING= 

3. Ensure the .env file is saved in the same directory as docker-compose.yml.

4. You can start the application using either Docker or Podman with the compose up command.
## Usage
1. After running docker compose up, the application will start and connect to the Neo4j database.
2. The chatbot will be available at http://localhost:8080.
3. The Neo4j database can be accessed at http://localhost:7474. You can view the database with a simple command like:
   ```sh
   MATCH (n) RETURN (n)
4. Upload a calibration certificate located in the Calibration Dataset of the root directory to the chatbot located in localhost:8080 to test the application.

