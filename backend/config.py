from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    Gemini_api_key: str= ""
    # Add other API keys or configurations here
    
    class Config:
        env_file = ".env"
settings = Settings()