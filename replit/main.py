from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(query: Query):
    return {
        "answer": f"(Mock) This is a placeholder answer for: '{query.question}'"
    }
