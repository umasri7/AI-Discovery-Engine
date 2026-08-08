def create_embedding(text):
    return get_model().encode([text])[0]