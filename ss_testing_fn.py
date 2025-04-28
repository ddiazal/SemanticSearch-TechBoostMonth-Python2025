import json
from semantic_search_fn import (
    create_data_texts,
    create_embedding,
    find_closest_n
)

# Data
products: str = "products.json"
# Query
query1: str = "High definition TV"
query2: str = "Skincare set"

# Fetch json data
with open(products) as f:
    data = json.load(f)

# Get data related texts
data_texts: list[str] = [create_data_texts(data_dict=d) for d in data]
# Generate data embeddings
data_embeddings: list[float] = create_embedding(texts=data_texts)
# Generate query embeddings
query_embeddings: list[float] = create_embedding(texts=query2)[0]

# Get top n query responses
hits = find_closest_n(
    query_vector=query_embeddings, embeddings=data_embeddings, n=3
)

sem_search: list = []
print(f'Search results for "{query2}"')
# Iterate over query responses
for hit in hits:
    product = data[hit["index"]]
    sem_search.append(product["title"])

# Print semantic search response
print(sem_search)