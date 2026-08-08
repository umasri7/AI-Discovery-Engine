from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def create_embedding(text):
    return vectorizer.fit_transform([text]).toarray()[0]