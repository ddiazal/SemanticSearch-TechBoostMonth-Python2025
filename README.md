# Semantic Search with Embeddings
## But, what is semantic search?
![Semantic Search Illustration](images/semanticSearch_metaImg.jpg)

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

### Windows
Open Command Prompt or PowerShell, then follow these steps:

1. Create and navigate to your project directory:

```cmd
mkdir project-semantic_search_w_embeddings
cd project-semantic_search_w_embeddings
```
2. Clone the repository:

```cmd
git clone https://github.com/ddiazal/SemanticSearch-TechBoostMonth-Python2025.git
```
3. Navigate into the cloned repository:

```cmd
cd SemanticSearch-TechBoostMonth-Python2025
```

4. Create a Python virtual environment inside the repository directory:

```cmd
python -m venv .venv
```
5. Activate the virtual environment:

```cmd
.venv\Scripts\activate
```
6. Upgrade pip and install all required packages:

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### UNIX
```shell
mkdir project-semantic_search_w_embeddings
cd project-semantic_search_w_embeddings
```
Clone repository from a URL
```shell
git clone https://github.com/ddiazal/SemanticSearch-TechBoostMonth-Python2025.git
```
Now, create a python virtual environment inside the repository directory:
```shell
cd SemanticSearch-TechBoostMonth-Python2025
python3 -m venv .venv
```
Activate your virtual environment
 ```shell
source .venv/bin/activate
```
Now, install all requirements so that you can run the scripts smoothly:
```shell
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the App
Now that your environment is ready and activated, it's time to execute a few more lines to have the app running.
Follow these steps in your PowerShell or terminal:

1. Initialize the `uvicorn` engine in your root folder to run the API:
```shell
python3 -m main
```
2. Now, in a new terminal/PowerShell tab in the git cloned repo folder run your `Streamlit` app!
```shell
streamlit run stapp.py
```
3. When you're done hit `Ctrl+c` on Windows/Linux or `^+c` on macOS to shutdown the process.


## Semantic Search API

```shell
curl -X POST http://localhost:8000/semantic-response \
    -H 'Content-Type:application/json' \
    -d '{"query":"Skincare set"}'
```
