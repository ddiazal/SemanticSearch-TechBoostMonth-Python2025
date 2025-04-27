# Semantic Search with Embeddings
## But, what is semantic search?
Semantic search is a `search technique that aims to understand the meaning and context of a user's query`, going beyond simple keyword matching to deliver more relevant results. It uses natural language processing (NLP) and machine learning (ML) to interpret the user's intent and provide results that align with their actual needs. 

## How does semantic search work?
Semantic search engines employ various techniques from natural language processing (NLP), knowledge representation, and machine learning to understand the semantics of search queries and web content. Here's a breakdown of the process:

* **Query analysis**: The search engine analyzes the user's query to identify keywords, phrases, and entities. It also attempts to interpret the user's search intent by analyzing the relationships between these elements.
* **Knowledge graph integration**: Semantic search engines often leverage knowledge graphs, vast databases containing information about entities and their relationships. This information helps the engine understand the context of the search query.
* **Content analysis**: Similar to how a search engine analyzes queries, it also examines the content of web pages to determine their relevance to a particular search. This analysis goes beyond keyword matching and considers factors such as the overall topic, sentiment, and entities mentioned within the content.
* **Result return and retrieval**: Based on the analysis of the query and the content, the search engine could return  web pages according to their relevance and semantic similarity to the search query. It then retrieves and displays the most relevant results to the user.

## And... What the hec are embeddings?
Embeddings are `numerical representations of data`, particularly text, images, or audio, that capture semantic relationships and allow machine learning models to understand and process complex information. They transform these inputs into vectors, which are then used to identify similarities and relationships between different pieces of data. 

### How they work:
* _Training_: Embeddings are created by training neural networks on large datasets. 
* _Vector Space_: The network learns to represent data as points in a high-dimensional vector space. 
* _Contextual Information_: The position of these points in the vector space reflects the semantic relationships and context of the data. 

## First steps
```shell
mkdir project-semantic_search_w_embeddings
cd project-semantic_search_w_embeddings
```
Now, create a python virtual environment:
```shell
python3 -m venv .venv
```
Activate your virtual environment
 ```shell
source .venv/bin/activate
```