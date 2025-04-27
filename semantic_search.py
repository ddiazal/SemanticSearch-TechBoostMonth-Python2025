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

class SemanticSearch:
    def __init__(self, client = emb_client):
        self.__client = client
        self.dataframe = None

    def __call__(self, data_file:str, query:str, file_type: str = "csv")->list[Any]:
        """_summary_

        Args:
            data_file (str): _description_
            query (str): _description_
            file_type (str, optional): _description_. Defaults to "csv".

        Returns:
            list[Any]: _description_
        """
        if file_type == "csv":
            self.dataframe: DataFrame = read_csv(data_file)
            data = self._fetch_into_json()
        else:
            with open(data_file) as f:
                data = json.load(f)

        data_texts: list[str] = [self.create_data_texts(data_dict=d) for d in data]
        data_embeddings: list[float] = self.create_embedding(texts=data_texts)[0]

        query_embeddings: list[float] = self.create_embedding(texts=query)[0]

        hits = self.find_closest_n(query_embeddings, data_embeddings, n=3)
        sem_search: list = []
        print(f'Search results for "{query}"')
        for hit in hits:
            product = data[hit["index"]]
            sem_search.append(product["title"])

        return sem_search


    def _fetch_into_json(self) -> list[dict[str, Any]]:
        """_summary_

        Returns:
            list[dict[str, Any]]: _description_
        """
        json_data = self.dataframe.to_json(orient='records')
        data:list[dict[str, Any]] = json.loads(json_data)
        return data


    @staticmethod
    def create_data_texts(data_dict: dict[str, Any]) -> str:
        """

        Args:
            data_dict (dict[str, Any]): _description_

        Returns:
            str: _description_
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
        """_summary_

        Args:
            texts (list | str): _description_

        Returns:
            list[Any]: _description_
        """
        response = self.__client.embeddings.create(
            model="text-embedding-3-small"
            ,input=texts
        )
        response_json = response.model_dump()
        return [response_data["embedding"] for response_data in response_json["data"]]


    @staticmethod
    def find_closest_n(query_vector: list[float], embeddings: list[float], n:int)->list[dict[str, Any]]:
        """_summary_

        Args:
            query_vector (list[float]): _description_
            embeddings (list[float]): _description_
            n (int): _description_

        Returns:
            list[dict[str, Any]]: _description_
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
