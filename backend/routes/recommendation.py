from fastapi import APIRouter
from services.recommendation_service import recommend_for_user

router = APIRouter()


@router.get("/recommend")
def recommend(product: str):

    user_history = [product]

    return recommend_for_user(user_history)