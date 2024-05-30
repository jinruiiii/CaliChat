# Calibration Certificate Key Extractor Chatbot

## Description
This project creates a chatbot that can extract key components from calibration certificates. The application is easy to use and is packaged in a Docker Compose format with two services: the actual application and a Neo4j database image pulled from Docker Hub.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

### Prerequisites
- Ensure you have [Docker](https://www.docker.com/get-started) of [Podman](https://docs.podman.io/en/latest/) installed on your machine.

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

4. You can start the application using either Docker or Podman with the compose up command
## Usage
1. After running docker compose up, the application will start and connect to the Neo4j database.
2. The chatbot will be available at http://localhost:8080.
3. The Neo4j database can be accessed at http://localhost:7474. You can view the database with a simple command like:
   ```sh
   MATCH (n) RETURN (n)

