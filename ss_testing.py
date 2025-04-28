import os
import pandas as pd
from semantic_search import SemanticSearch

# Get OpenAI secret key
SECRET_KEY: str = os.getenv("OPI_OPENAI_API_KEY")
print(SECRET_KEY)

# Instantiate class
sem_search = SemanticSearch()

# Data
products: str = "products.json"
# Query
query: str = "High definition TV"

query_response = sem_search(
    data_file=products, query=query, file_type="json"
)

print(query_response)
