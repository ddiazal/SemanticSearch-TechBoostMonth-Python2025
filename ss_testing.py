from semantic_search import SemanticSearch

# Instantiate class
sem_search = SemanticSearch()

# Data to query
products: str = "products.json"
# Test queries
query1: str = "High definition TV"
query2: str = "Skincare set"

# Get top n query responses
query_response = sem_search(
    data_file=products, query=query2, file_type="json"
)

# Print semantic search response
print(query_response)
