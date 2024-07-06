import pymongo
import openai

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
mongodb_uri = os.getenv("MONGODB_URI")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = pymongo.MongoClient(mongodb_uri)
db = client.sample_mflix
coll = db.embedded_movies


def generate_query_embedding_openai(query: str) -> list[float]:
    client = openai.OpenAI(api_key=openai_api_key)
    response = client.embeddings.create(model="text-embedding-ada-002", input=query)
    response_dict = response.to_dict()  # Convert response to dictionary
    embedding = response_dict['data'][0]['embedding']
    return embedding
	

query = "What is the plot of the movie with the title 'The Shawshank Redemption'?"

result = coll.aggregate([
    {"$vectorSearch": {
        "queryVector": generate_query_embedding_openai(query),
        "path": "plot_embedding",
        "numCandidates": 100,
        "limit": 4,
        "index": "PlotSemanticSearch2"
    }}
])

for doc in result:
    print(f"Movie: {doc['title']}\nPlot: {doc['plot']}\n")