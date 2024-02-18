from fastapi import FastAPI
from .auth import sign_up, sign_in, create_api_key

users_app = FastAPI()

@users_app.post('/sign_up')
def sign_up_endpoint(*args, **kwargs):
    return sign_up(*args, **kwargs)

@users_app.post('/sign_in')
def sign_in_endpoint(*args, **kwargs):
    return sign_in(*args, **kwargs)

@users_app.post('/create_api_key')
def create_api_key_endpoint(*args, **kwargs):
    return create_api_key(*args, **kwargs)
