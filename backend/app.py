from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.recommendation import router as recommendation_router
from routes.search import router as search_router

app = FastAPI(
    title="AI Discovery Engine",
    version="1.0" 
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(search_router)
app.include_router(recommendation_router)


def home():

    return {
        "message": "AI Discovery Engine Running"
    }