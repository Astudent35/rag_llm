from pymongo import MongoClient
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import OpenAI
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
ATLAS_VECTOR_SEARCH_INDEX_NAME = "project2"
collection = client[db_name][collection_name]

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
# vector_search = MongoDBAtlasVectorSearch(collection, embeddings)

vector_search = MongoDBAtlasVectorSearch.from_connection_string(
    mongodb_uri,
    db_name + "." + collection_name,
    OpenAIEmbeddings(disallowed_special=()),
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)

def query_data(query):
    docs = vector_search.similarity_search(query, k=1)
    if docs:
        as_output = docs[0].metadata
    else:
        as_output = "No documents found."

    llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
    retriever = vector_search.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )
    result = qa({"query": query})

    print("Result: ", result)  # Debugging: Check the result from QA
    return result["result"], result["source_documents"]

# ... existing code ...


with gr.Blocks(theme="base", title="Query Data Interface: answering using Vector Search + RAG") as app:
    gr.Markdown("## Query Data Interface")
    query = gr.Textbox(lines=2, placeholder="Enter your query here...")
    with gr.Row():
        submit_button = gr.Button("Submit")
        clear_button = gr.Button("Clear")
    with gr.Column():
        output_2 = gr.Textbox(lines=2, placeholder="Answer from RAG")
        output = gr.Textbox(lines=2, placeholder="Documents from atlas")

    submit_button.click(fn=query_data, inputs=[query], outputs=[output2, output])

app.launch()