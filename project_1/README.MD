Sure! Here is a `README.md` file for your project:

```markdown
# Movie Recommendations with OpenAI and MongoDB

This project demonstrates how to use OpenAI's API to generate embeddings for movie plot queries and perform a vector search in a MongoDB collection to find similar movies.

## Prerequisites

- Python 3.7+
- MongoDB
- OpenAI API Key
- `.env` file with the following variables:
  - `MONGODB_URI`: Your MongoDB connection string
  - `OPENAI_API_KEY`: Your OpenAI API key

## Installation

1. Clone the repository:
    ```sh
    git clone 
    cd movie-recs-openai
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your MongoDB URI and OpenAI API key:
    ```env
    MONGODB_URI=your_mongodb_uri
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the script:
    ```sh
    python project_1/movie_recs_openai.py
    ```

2. The script will output the titles and plots of the top 4 movies that are semantically similar to the query.

## Code Explanation

- **Environment Setup**: Load environment variables from a `.env` file.
- **Database Connection**: Connect to a MongoDB database and select the `embedded_movies` collection.
- **OpenAI Embedding Generation**: Use OpenAI's API to generate embeddings for the query.
- **Vector Search**: Perform a vector search in the MongoDB collection using the generated embeddings.
- **Output**: Print the titles and plots of the top 4 similar movies.

## Example

```sh
Movie: The Shawshank Redemption
Plot: Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.

Movie: The Green Mile
Plot: The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.

...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to customize the `README.md` file as needed for your project.