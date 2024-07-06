```markdown:project_2/README.md
# Project 2

## Overview
This project demonstrates the use of LangChain, OpenAI, and MongoDB Atlas Vector Search to create a document retrieval and question-answering system. The system loads documents, generates embeddings, stores them in MongoDB Atlas, and provides a Gradio interface for querying the data.

## Files

### `extract_information.py`
This script is responsible for setting up the MongoDB connection, loading environment variables, initializing the vector search, and defining the query function. It also sets up a Gradio interface for querying the data.

#### Key Sections:
- Importing necessary libraries and modules.
- Loading environment variables.
- Initializing MongoDB client and vector search.
- Defining the `query_data` function to perform similarity search and question answering.
- Setting up the Gradio interface.

Relevant code blocks:
```python:project_2/extract_information.py
startLine: 1
endLine: 67
```

### `load_data.py`
This script handles loading documents from a directory, generating embeddings for the documents, and storing them in MongoDB Atlas Vector Search.

#### Key Sections:
- Importing necessary libraries and modules.
- Loading environment variables.
- Initializing MongoDB client.
- Loading documents from a specified directory.
- Generating embeddings and storing them in MongoDB Atlas.

Relevant code blocks:
```python:project_2/load_data.py
startLine: 1
endLine: 27
```

### `sample_files/`
This directory contains sample text files used for loading and testing the document retrieval system.

#### Files:
- `aerodynamics.txt`: Contains information about aerodynamics.
- `log_example.txt`: Contains log entries for the data loading process.
- `chat_conversation.txt`: Contains a sample chat conversation.

Relevant code blocks:
```python:project_2/sample_files/aerodynamics.txt
startLine: 1
endLine: 14
```
```python:project_2/sample_files/log_example.txt
startLine: 1
endLine: 11
```
```python:project_2/sample_files/chat_conversation.txt
startLine: 1
endLine: 10
```

## Setup

1. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages using pip:
   ```sh
   pip install pymongo langchain_community langchain_openai gradio python-dotenv
   ```

2. **Environment Variables**:
   Create a `.env` file in the root directory and add your MongoDB URI and OpenAI API key:
   ```
   MONGODB_URI=your_mongodb_uri
   OPENAI_API_KEY=your_openai_api_key
   ```

3. **Load Data**:
   Run the `load_data.py` script to load documents, generate embeddings, and store them in MongoDB Atlas:
   ```sh
   python project_2/load_data.py
   ```

4. **Run the Application**:
   Run the `extract_information.py` script to start the Gradio interface:
   ```sh
   python project_2/extract_information.py
   ```

## Usage
- Open the Gradio interface in your browser.
- Enter your query in the provided textbox and click "Submit".
- The interface will display the answer from the retrieval-augmented generation (RAG) model and the relevant documents from MongoDB Atlas.

## License
This project is licensed under the MIT License.
```
