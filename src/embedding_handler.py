from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

def get_embeddings(questions):
    return model.encode(questions, convert_to_numpy=True)

def create_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def add_to_index(index, embeddings, new_embedding):
    index.add(new_embedding)
    embeddings = np.vstack((embeddings, new_embedding))
    return index, embeddings
