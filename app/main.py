from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.v1 import chat


app = FastAPI(title="MediAI SmartAssist LLM Service")

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])