from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
mongodb_uri = os.getenv("MONGODB_URI")
openai_api_key = os.getenv("OPENAI_API_KEY")


client = MongoClient(mongodb_uri)
db_name = "langchain_demo"
collection_name = "collection_of_text_blobs"
collection = client[db_name][collection_name]

loader = DirectoryLoader("./sample_files", glob="**/*.txt", show_progress=True)
documents = loader.load()

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

vector_db = MongoDBAtlasVectorSearch.from_documents(documents, embeddings, collection=collection)