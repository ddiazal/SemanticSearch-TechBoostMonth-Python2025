from pydantic import BaseModel

class SemanticResponseModel(BaseModel):
    semantic_response: dict[str, list[str]]

class UserQuery(BaseModel):
    query: str