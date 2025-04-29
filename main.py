import uvicorn
from fastapi import FastAPI, Request
from semantic_search import SemanticSearch
from fastapi.responses import JSONResponse
from Models import SemanticResponseModel, UserQuery

app = FastAPI(title='Semantic Search API')
sem_search = SemanticSearch()

@app.get("/")
async def root():
    return {"status": "healthy", "service": "Semantic Search API"}


@app.post("/semantic-response", response_model=SemanticResponseModel)
def semantic_response(data: UserQuery):
    # Data to query
    user_query: str = data.query
    model_response: list[str] = sem_search(
        data_file="products.json", query=user_query, file_type="json"
    )
    sm_response = {
        "semantic_response": {
            "response": model_response
        }
    }
    return sm_response


@app.exception_handler(Exception)
async def http_exception_handler(request: Request, exc: Exception):
    return JSONResponse(content={"error": f"Internal Server Error: {str(exc)}"}, status_code=500)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
