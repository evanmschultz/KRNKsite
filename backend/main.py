from fastapi import FastAPI, Request, Response
from sqlalchemy import create_engine
from config.database import Base, SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI App
app = FastAPI()

# Define the list of allowed origins for CORS
origins = ["http://localhost:3000"]

from app.models.user import User
from app.models.topic import Topic
from app.models.paper import Paper
from app.models.summary import Summary
from app.models.associations import Base
from app.schemas.user_schema import UserCreateSchema, UserResponseSchema

# Create the database tables
Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next) -> Response:
    """
    Middleware to manage database sessions.

    This middleware attaches a new SQLAlchemy session to each incoming HTTP request
    by storing it in `request.state.db`. The session is closed when the request is
    finished. This ensures that you can access the DB session by referencing `request.state.db`
    within the scope of a request.

    Args:
        request (Request): The incoming request object provided by FastAPI.
        call_next: A function to call the next middleware or route.

    Returns:
        Response: The outgoing response object.
    """
    response: Response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import your routers here
from app.routes.users import router as user_router

# Include the routers in the app
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
# app.include_router(topic_router)
# app.include_router(paper_router)
