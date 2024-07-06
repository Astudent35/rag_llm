import pymongo
import requests

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
mongodb_uri = os.getenv("MONGODB_URI")
hf_token = os.getenv("HUGGING_FACE_TOKEN")

client = pymongo.MongoClient(mongodb_uri)
db = client.sample_mflix
coll = db.movies


EMBEDDING_API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {hf_token}"}


def generate_query_embedding(payload: dict) -> list[float]:
	response = requests.post(EMBEDDING_API_URL, headers=headers, json=payload)
	if response.status_code != 200:
		raise ValueError(f"Failed to get embedding for text: {payload}")
	return response.json()
	

# NOTE: Uncomment the following code to generate the embeddings for the movies
# for doc in coll.find({"plot": {"$exists": True}}).limit(50):
#     doc["embedding"] = query({
#         "inputs": {
#             "source_sentence": doc["plot"],
#             "sentences": [doc["plot"] for doc in coll.find({"plot": {"$exists": True}}).limit(384)]
#         }
#     })
#     coll.replace_one({"_id": doc["_id"]}, doc)
#     print(doc)

query = "What is the plot of the movie with the title 'The Shawshank Redemption'?"

result = coll_2.aggregate([
    {"$vectorSearch": {
        "queryVector": generate_query_embedding({
            "inputs": {
                "source_sentence": query,
                "sentences": [doc["plot"] for doc in coll_2.find({"plot": {"$exists": True}}).limit(384)]
            }
        }),
        "path": "embedding",
        "numCandidates": 100,
        "limit": 4,
        "index": "PlotSemanticSearch2"
    }}
])

for doc in result:
    print(f"Movie: {doc['title']}\nPlot: {doc['plot']}\n")