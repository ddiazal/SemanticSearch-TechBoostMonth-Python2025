import os
import json
from typing import Any
from openai import OpenAI
from pandas import DataFrame
from operator import itemgetter
from scipy.spatial import distance

# Get OpenAI secret key
SECRET_KEY: str = os.getenv("OPI_OPENAI_API_KEY")
# Instantiate OpenAI client
emb_client = OpenAI(
    api_key=SECRET_KEY,
)

def _fetch_into_json(dataframe: DataFrame) -> list[dict[str, Any]]:
    """Transform a Dataframe into a list of dictionaries.

    Returns:
        list[dict[str, Any]]: list of dictionaries or JSON objects.
    """
    json_data = dataframe.to_json(orient='records')
    data: list[dict[str, Any]] = json.loads(json_data)
    return data


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


def create_embedding(texts: list | str) -> list[Any]:
    """Generate embedding from texts.

    Args:
        texts (list | str): A list of texts or a single text.

    Returns:
        list[Any]: List of vectors embeddings corresponding to each text.
    """
    response = emb_client.embeddings.create(
        model="text-embedding-3-small"
        , input=texts
    )
    response_json = response.model_dump()
    return [response_data["embedding"] for response_data in response_json["data"]]


def find_closest_n(query_vector: list[float], embeddings: list[float], n: int) -> list[dict[str, Any]]:
    """_Find top n responses using cosine distance to compare query vectors embeddings and
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

