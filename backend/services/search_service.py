from models.semantic_search import search_products

def semantic_search(query):

    results = search_products(query)

    return {
        "query": query,
        "total_results": len(results),
        "products": results
    }