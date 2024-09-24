***AI Chat Bot for Querying Internal Knowledge Bases in Atlassian Confluence***



This project implements an AI chatbot that uses a locally hosted Large Language Model (LLM) to query internal knowledge bases, specifically those in Atlassian Confluence. The chatbot retrieves domain-specific information from internal knowledge bases, processes it through vector embeddings, and generates responses using a locally hosted LLM, making it suitable for internal enterprise use.
Key Features

    Domain-specific AI chat bot that answers queries using internal knowledge bases.
    Uses Chroma DB as the vector database for storing and querying knowledge chunks.
    Powered by Lang-chain and Ollama for LLM prompting and processing.
    Streamlit-based front-end for easy interaction.
    Support for large language models like Mistral and Llama.
    Nomic Embed for embedding text data into vectors.


How It Works

    Data Storage in Vector Database: Internal knowledge base documents are first embedded using a text embedding model like Nomic Embed. The embedded vectors are stored in Chroma DB.
    Query Processing: When the user submits a query, the chatbot retrieves the most relevant knowledge chunks from the vector database by comparing vector embeddings with the user’s query.
    Prompt Generation: The retrieved knowledge chunks are used to generate a prompt.
    Answer Generation: The prompt is then processed by the internally hosted LLM (e.g., Mistral or Llama), which generates an accurate, domain-specific response.

Project Structure

├── app.py                      # Chat interface using Streamlit

├── get_embedding.py            # Function to query the vector database to get relevant embeddings

├── populate_database.py        # Script to populate the vector database

├── query_data.py               # Generate a prompt and query the large language model

├── test_rag.py                 # Test the RAG model

├── requirements.txt            # Dependencies for the project

├── data/                       # Folder to add documents (internal knowledge base)

└── chroma/                     # Folder where the vector database is created


Dependencies

    Python
    Streamlit
    Lang-chain
    Ollama
    Chroma DB
    Mistral
    Llama
    Nomic Embed

To see the complete list of dependencies, check the requirements.txt file.


---How to run the application---


1. Clone the Repository

First, clone this repository to your local machine:

git clone https://github.com/madushanka-samarajeewa/chat_bot.git
cd chat_bot

2. Create Python Virtual Environment

It is recommended to use a virtual environment to manage project dependencies:
python -m venv venv

Activate the virtual environment:

    For Windows: venv\Scripts\activate
    For macOS/Linux: source venv/bin/activate
    
3. Create Required Folders

You'll need to create two folders: data to store documents, and chroma to store the vector database. Run the following commands:

4.Install Dependencies

To install the required dependencies, use:

    pip install -r requirements.txt
5. Populate the Vector Database

Before running the chatbot, you must populate the vector database with internal knowledge base data. You can do this using the populate_database.py script:

6. Running the Streamlit Application 

       streamlit run app.py



