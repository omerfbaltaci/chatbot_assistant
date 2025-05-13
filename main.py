from src.helpers import load_json
from src.search_engine import build_faiss_index, search
from src.config import ORIGINAL_DATA_PATH, EXTENDED_DATA_PATH

def main():

    while True:
        original_data = load_json(ORIGINAL_DATA_PATH)
        extended_data = load_json(EXTENDED_DATA_PATH)
        full_data = original_data + extended_data
        
        index, embeddings = build_faiss_index(full_data)
        
        user_question = input("\nSoru girin (çıkmak için 'q'): ")
        if user_question.lower() == "q":
            break

        answer, source, score = search(
            user_question,
            full_data,
            index,
            embeddings,
            EXTENDED_DATA_PATH,
            extended_data
        )

        print("\n--- CEVAP ---")
        print(f"Cevap: {answer}")
        print(f"Kaynak: {source} | Benzerlik: {round(score, 3)}")

if __name__ == "__main__":
    main()
