from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import router
from app.database import engine
from app.models import Base
from app.seed import seed_if_empty

app = FastAPI(title="AI Helpdesk Chatbot", version="1.0.0")

app.add_middleware(
	CORSMiddleware,
	allow_origins=[o.strip() for o in settings.cors_origins.split(",")],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.on_event("startup")
def startup():
	Base.metadata.create_all(bind=engine)
	if settings.demo_seed:
		seed_if_empty()


app.include_router(router)
