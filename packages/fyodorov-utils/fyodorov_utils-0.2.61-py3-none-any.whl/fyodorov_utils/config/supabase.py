from supabase import create_client, Client
from .config import Settings

settings = Settings()

def get_supabase(key: str = None) -> Client:
    if key:
        return create_client(
            settings.SUPABASE_URL,
            key,
        )
    else:
        return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
