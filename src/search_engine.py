from src.embedding_handler import get_embeddings, create_index, add_to_index
from src.helpers import is_technical_question, truncate, save_json
from src.llm_api import ask_llm

def build_faiss_index(full_data):
    questions = [item["question"] for item in full_data]
    embeddings = get_embeddings(questions)
    index = create_index(embeddings)
    return index, embeddings

def search(user_question, full_data, index, embeddings, extended_data_path, extended_data):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
    user_embedding = model.encode([user_question], convert_to_numpy=True)

    distances, indices = index.search(user_embedding, k=1)
    score = 1 - (distances[0][0] / 2) # cosine similarity yerine euclidian distance (FlatIP yerine L2 ile)

    if score >= 0.90:
        match = full_data[indices[0][0]]
        return match["answer"], "dataset", score

    if not is_technical_question(user_question):
        return "Bu soru teknik bir soru gibi görünmüyor. Lütfen C# veya .NET hakkında soru sorunuz.", "not_technical", score

    if score < 0.70:
        return "Soru yeterince teknik değil veya çok belirsiz. Daha açık yazmayı deneyin.", "low_similarity", score

    # LLM’den cevap al
    print("Sorulan teknik soru veri setinde mevcut değil, harici yapay zeka modeline soruluyor...\n")
    answer = ask_llm(f"Cevap verirken kısa, net ve teknik detay ver. Olabildiğince kısa tut. Soru şu: {user_question}")
    answer = truncate(answer)

    # Kaydet
    new_item = {
        "question": user_question,
        "answer": answer,
        "embedding_score": float(score)
    }
    extended_data.append(new_item)
    save_json(extended_data_path, extended_data)

    # Index’e ekle
    index, embeddings = add_to_index(index, embeddings, user_embedding)

    return answer, "llm", score
