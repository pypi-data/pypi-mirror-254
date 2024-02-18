from pydantic_settings import BaseSettings
import os

print(f"Loading settings from .env")
print(f"Working directory: {os.getcwd()}")
print(f"Supabase project URL: {os.getenv('SUPABASE_PROJECT_URL')}")

class Settings(BaseSettings):
    SUPABASE_URL: str = os.getenv("SUPABASE_PROJECT_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_API_KEY")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
