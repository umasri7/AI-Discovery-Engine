import pandas as pd
import numpy as np
import faiss

from models.embeddings import create_embedding

# Load products
products = pd.read_csv("data/products.csv")

# Create embeddings
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

# Create FAISS Index
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)


def search_products(query, k=5):

    query_vector = create_embedding(query).astype("float32")

    distances, indices = index.search(
        np.array([query_vector]),
        k
    )

    results = products.iloc[indices[0]]

    return results.to_dict(orient="records")