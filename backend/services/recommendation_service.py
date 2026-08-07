from models.semantic_search import search_products

def recommend_for_user(user_history):

    recommendations = []

    for item in user_history:
        results = search_products(item, k=2)

        recommendations.extend(results)

    # Remove duplicates
    unique = []
    seen = set()

    for product in recommendations:
        product_id = product["id"]

        if product_id not in seen:
            seen.add(product_id)
            unique.append(product)

    return {
        "history": user_history,
        "recommendations": unique
    }