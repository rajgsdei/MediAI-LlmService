from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    query: str
    
    
@router.post("/")
def chat_response(request: ChatRequest):
    """
    Process the chat request and return a response.
    """
    # Here you would typically call your LLM service to get a response
    response = f"Response to: {request.query}"
    return {"response": response}