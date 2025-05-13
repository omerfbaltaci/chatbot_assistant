from sentence_transformers import SentenceTransformer
from google import generativeai as genai
from dotenv import load_dotenv
import numpy as np
import faiss
import json
import os

model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


original_data_path = "data/data.json"
if os.path.exists(original_data_path):
    with open(original_data_path, "r", encoding="utf-8") as f:
        original_data = json.load(f)
else:
    original_data = []
    
    
extended_data_path = "data/extended_data.json"
if os.path.exists(extended_data_path):
    with open(extended_data_path, "r", encoding="utf-8") as f:
        extended_data = json.load(f)
else:
    extended_data = []


full_dataset = original_data + extended_data

questions = [item["question"] for item in full_dataset]
answers = [item["answer"] for item in full_dataset] # Henüz kullanmadım

embeddings = model.encode(questions, convert_to_numpy=True)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Teknik konulara özel anahtar kelimeler
technical_keywords = [
    "c#", ".net", "asp.net", "mvc", "razor", "entity framework", "asp",
    "viewbag", "viewdata", "controller", "model", "startup.cs", "configure", "linq",
    "taghelper", "dependency injection", "middleware", "async", "await", "partialview"
]

SIMILARITY_THRESHOLD = 0.90
TECHNIC_SIMILARITY_THRESHOLD = 0.70

def is_technical(question: str) -> bool:
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in technical_keywords)

def ask_llm(prompt: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"API hatası: {e}")
        return "Şu anda dış API'ye erişilemedi. Lütfen daha sonra tekrar deneyin."

def update_index(new_question):
    global index, embeddings
    new_embedding = model.encode([new_question], convert_to_numpy=True)
    embeddings = np.vstack((embeddings, new_embedding))
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

def filter_gemini_response(response: str) -> str:
    if len(response) > 500:
        response = response[:497] + "..."
    
    response = response.replace("\n\n", "\n").strip()
    return response

def search_question(user_question: str):
    user_embedding = model.encode([user_question], convert_to_numpy=True)
    distances, indices = index.search(user_embedding, k=1)
    score = 1 - (distances[0][0] / 2)  # Sırf cos_sim fonksiyonu için PyTorch'u import etmek istemedim.

    if score >= SIMILARITY_THRESHOLD:
        matched = full_dataset[indices[0][0]]
        return {
            "answer": matched["answer"],
            "source": "dataset",
            "score": float(round(score, 3)),
            "note": "Bu cevap veri setinde halihazırda bulundu."
        }
    elif is_technical(user_question):
        
        if score <= TECHNIC_SIMILARITY_THRESHOLD: # Soru sırf belirli kelimeleri içerdiğinden teknik sayılsa bile, eğer teknik bir soru değilse GeminiAPI'ye gitmemesi için.
            return {
                "answer": "Bu soru teknik kelimeler içeriyor ancak tam olarak teknik bir soru değil. Lütfen daha spesifik bir teknik soru sorun.",
                "source": "none",
                "score": float(score),
                "note": "Yetersiz benzerlik skoru."
            }
        else:
            print("Sorulan teknik soru veri setinde mevcut değil, harici yapay zeka modeline soruluyor...\n")
            answer = ask_llm(f"Cevap verirken kısa, net ve teknik detay ver. Olabildiğince kısa tut. Soru şu: {user_question}")
            answer = filter_gemini_response(answer)
            
            new_item = {
                "question": user_question,
                "answer": answer,
                "embedding_score": float(score)
            }
            extended_data.append(new_item)
            
            try:
                with open(extended_data_path, "w", encoding="utf-8") as f:
                    json.dump(extended_data, f, ensure_ascii=False, indent=2)
            except Exception as e:
                    print(f"Dosya yazma hatası: {e}")
                
            update_index(user_question)
                
            return {
                "answer": answer,
                "source": "gemini",
                "score": round(score, 3),
                "note": "Cevap Gemini API'den alındı ve veri setine kaydedildi."
            }
    else:
        return {
            "answer": "Bu soru C# ya da .NET hakkında görünmüyor. Lütfen teknik bir soru sorunuz.",
            "source": "none",
            "score": 0,
            "note": "Teknik olmayan bir soru tespit edildi."
        }

# Test
def test():
    if __name__ == "__main__":
        while True:
            q = input("\nSorunuzu giriniz (çıkmak için 'q' girebilirsiniz): ")
            if q.lower() == "q":
                break
            result = search_question(q)
            print("\n--- CEVAP ---")
            print(f"Cevap: {result['answer']}")
            print(f"Kaynak: {result['source']} | Skor: {result['score']}")
            print(f"Açıklama: {result['note']}")

test()
