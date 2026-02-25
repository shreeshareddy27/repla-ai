from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Ollama API
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"   # model you tested earlier


# Request format
class EmailRequest(BaseModel):
    email_body: str
    tone: str = "professional"


@app.get("/")
def home():
    return {"status": "Backend running"}


@app.post("/generate-reply")
def generate_reply(data: EmailRequest):

    prompt = f"""
Write a {data.tone} email reply to the following message:

Email:
{data.email_body}

Reply:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return {
        "reply": result["response"]
    }