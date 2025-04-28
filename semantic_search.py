import os
import json

from typing import Any

from openai import OpenAI
from pandas import read_csv
from pandas import DataFrame
from operator import itemgetter
from scipy.spatial import distance

# Get OpenAI secret key
SECRET_KEY: str = os.getenv("OPI_OPENAI_API_KEY")
# Instantiate OpenAI client
emb_client = OpenAI(
    api_key=SECRET_KEY,
)

# Create semantic search class
class SemanticSearch:
    def __init__(self, client = emb_client):
        # Class attributes
        self.__client = client
        self.dataframe = None

    def __call__(self, data_file:str, query:str, file_type: str = "csv")->list[Any]:
        """Special method that allows instances of a class to be called like regular functions.
        This enables objects to behave like functions, providing a flexible way to encapsulate
        functionality.

        Args:
            data_file (str): Data to query over.
            query (str): User query string.
            file_type (str, optional): File extension. Defaults to "csv".

        Returns:
            list[Any]: Semantic search results.
        """
        if file_type == "csv":
            self.dataframe: DataFrame = read_csv(data_file)
            data = self._fetch_into_json()
        else:
            with open(data_file) as f:
                data = json.load(f)

        # Get data related texts
        data_texts: list[str] = [self.create_data_texts(data_dict=d) for d in data]
        # Generate data embeddings
        data_embeddings: list[float] = self.create_embedding(texts=data_texts)
        # Generate query embeddings
        query_embeddings: list[float] = self.create_embedding(texts=query)[0]

        # Get top n query responses
        hits = self.find_closest_n(
            query_vector=query_embeddings, embeddings=data_embeddings, n=3
        )
        sem_search: list = []
        print(f'Search results for "{query}"')
        # Iterate over query responses
        for hit in hits:
            product = data[hit["index"]]
            sem_search.append(product["title"])

        # Return semantic search response
        return sem_search


    # Class private method
    def _fetch_into_json(self) -> list[dict[str, Any]]:
        """Transform a Dataframe into a list of dictionaries.

        Returns:
            list[dict[str, Any]]: list of dictionaries or JSON objects.
        """
        json_data = self.dataframe.to_json(orient='records')
        data:list[dict[str, Any]] = json.loads(json_data)
        return data


    @staticmethod
    def create_data_texts(data_dict: dict[str, Any]) -> str:
        """Generate data related texts.

        Args:
            data_dict (dict[str, Any]): Data dictionary or JSON object.

        Returns:
            str: Formatted string containing keywords for search.
        """
        (
            title,
            short_description,
            features
        ) = itemgetter(
            'title',
            'short_description',
            'features')(data_dict)
        return f"""Title: {title}
        Description: {short_description}
        Features: {', '.join(features)}"""


    def create_embedding(self, texts: list | str)->list[Any]:
        """Generate embedding from texts.

        Args:
            texts (list | str): A list of texts or a single text.

        Returns:
            list[Any]: List of vectors embeddings corresponding to each text.
        """
        response = self.__client.embeddings.create(
            model="text-embedding-3-small"
            ,input=texts
        )
        response_json = response.model_dump()
        return [response_data["embedding"] for response_data in response_json["data"]]


    @staticmethod
    def find_closest_n(query_vector: list[float], embeddings: list[float], n:int)->list[dict[str, Any]]:
        """Find top n responses using cosine distance to compare query vectors embeddings and
        data embeddings.

        Args:
            query_vector (list[float]): Query vector embeddings.
            embeddings (list[float]): Data vector embeddings.
            n (int): Number of top responses to return.

        Returns:
            list[dict[str, Any]]: List of semantic search results.
        """
        distances: list[dict[str, Any]] = []
        for index, embedding in enumerate(embeddings):
            # Calculate the cosine distance between the query vector and embedding
            dist = distance.cosine(query_vector, embedding)
            # Append the distance and index to distances
            distances.append({"index": index, "distance": dist})
        # Sort distances by the distance key
        sorted_distances = sorted(distances, key=lambda d: d["distance"])
        # Return the first n elements in distances_sorted
        return sorted_distances[:n]
