from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    n8n_chat_webhook_url: str
    n8n_create_ticket_webhook_url: str
    n8n_ticket_status_webhook_url: str
    embedding_model: str = "all-MiniLM-L6-v2"
    cors_origins: str = "http://localhost:5173"
    demo_seed: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
