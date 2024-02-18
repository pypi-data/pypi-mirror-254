from supabase import create_client, Client
from .config import Settings

settings = Settings()

def get_supabase(jwt: str = None) -> Client:
    if jwt:
        return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY, headers={"Authorization": f"Bearer {jwt}"})
    else:
        return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
