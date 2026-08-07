import os
import faiss
import numpy as np
import pandas as pd

from models.embeddings import create_embedding

INDEX_PATH = "vector_db/faiss_index.bin"
DATA_PATH = "data/products.csv"


def build_index():
    products = pd.read_csv(DATA_PATH)

    vectors = []

    for _, row in products.iterrows():

        text = (
            row["name"] + " " +
            row["category"] + " " +
            row["brand"] + " " +
            row["description"]
        )

        vectors.append(create_embedding(text))

    vectors = np.array(vectors).astype("float32")

    index = faiss.IndexFlatL2(vectors.shape[1])

    index.add(vectors)

    faiss.write_index(index, INDEX_PATH)

    print("✅ FAISS Index Saved")

    return index


def load_index():

    if os.path.exists(INDEX_PATH):
        try:
            print("✅ Loading Existing FAISS Index")
            return faiss.read_index(INDEX_PATH)

        except Exception:
            print("❌ Corrupted FAISS Index Found")
            print("⚡ Rebuilding Index...")
            return build_index()

    print("⚡ Creating New FAISS Index")
    return build_index()