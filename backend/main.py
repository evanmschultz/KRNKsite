from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from config.database import Base, SessionLocal, engine

# Initialize FastAPI App
app = FastAPI()


# Debug middleware for printing headers should be the first middleware
@app.middleware("http")
async def debug_headers(request: Request, call_next):
    print("Incoming Request Headers:", request.headers)
    return await call_next(request)


# Middleware to manage database sessions
@app.middleware("http")
async def db_session_middleware(request: Request, call_next) -> Response:
    """
    Middleware to manage database sessions.
    """
    response: Response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# CORS Middleware settings
origins = [
    "http://localhost:3000",  # The origin where your frontend runs
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.models.user import User
from app.models.topic import Topic
from app.models.paper import Paper
from app.models.summary import Summary
from app.models.associations import Base
from app.schemas.user_schema import UserCreateSchema, UserResponseSchema

# Create the database tables
Base.metadata.create_all(bind=engine)

from app.routes.users import router as user_router

# Include the routers in the app
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
# app.include_router(topic_router)
# app.include_router(paper_router)
