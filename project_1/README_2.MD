Sure! Here is a `README.md` file for your project:

```markdown
# Movie Recommendations

This project provides a way to generate and search for movie plot embeddings using the Hugging Face API and MongoDB.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your MongoDB URI and Hugging Face token:**
    ```env
    MONGODB_URI=your_mongodb_uri
    HUGGING_FACE_TOKEN=your_hugging_face_token
    ```

## Usage

### Generating Embeddings for Movies

To generate embeddings for the movies in your MongoDB collection, uncomment the following code in `movie_recs.py`:

```python
# for doc in coll.find({"plot": {"$exists": True}}).limit(50):
#     doc["embedding"] = query({
#         "inputs": {
#             "source_sentence": doc["plot"],
#             "sentences": [doc["plot"] for doc in coll.find({"plot": {"$exists": True}}).limit(384)]
#         }
#     })
#     coll.replace_one({"_id": doc["_id"]}, doc)
#     print(doc)
```

Run the script to generate and store the embeddings in your MongoDB collection.

### Searching for Movie Plots

To search for movie plots using a query, modify the `query` variable in `movie_recs.py`:

```python
query = "What is the plot of the movie with the title 'The Shawshank Redemption'?"
```

Run the script to get the search results:

```sh
python movie_recs.py
```

The script will print the titles and plots of the top matching movies.

## Dependencies

- `pymongo`
- `requests`
- `python-dotenv`

Make sure to install these dependencies using the `requirements.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` provides an overview of the project, setup instructions, usage details, and information about dependencies and licensing. Adjust the `<repository_url>` and `<repository_directory>` placeholders as needed.