from fastapi import APIRouter

from services.search_service import semantic_search

router = APIRouter()


@router.get("/search")
def search(query: str):

    return semantic_search(query)