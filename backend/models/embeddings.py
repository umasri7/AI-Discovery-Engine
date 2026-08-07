from sentence_transformers import SentenceTransformer

print("Loading AI Model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!")

def create_embedding(text):
    """
    Convert text into an embedding vector.
    """
    return model.encode(text)