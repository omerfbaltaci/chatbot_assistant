# app.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.helpers import load_json, save_json
from src.embedding_handler import get_embeddings, create_index
from src.search_engine import search
from src.llm_api import ask_llm
from src.config import ORIGINAL_DATA_PATH, EXTENDED_DATA_PATH
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

app = FastAPI()

# Veri yükleme
data = load_json(ORIGINAL_DATA_PATH)
extended_data = load_json(EXTENDED_DATA_PATH)
full_data = data + extended_data

# Embedding oluştur
questions = [item['question'] for item in full_data]
answers = [item['answer'] for item in full_data]
embeddings = get_embeddings(questions)
index = create_index(embeddings)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question

    try:
        answer, source, score = search(
            question,
            full_data,
            index,
            embeddings,
            EXTENDED_DATA_PATH,
            extended_data
        )
        return {
            "answer": answer,
            "source": source,
            "score": float(score)
        }
    except Exception as e:
        return {"error": str(e)}
