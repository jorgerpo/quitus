from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from app.config import config

apikey_scheme = APIKeyHeader(name=config.APIKEY_HEADER_NAME)


def check_token(token: str = Security(apikey_scheme)):
    if token != config.APIKEY_HEADER_TOKEN:
        raise HTTPException(status_code=403, detail="Access Forbidden")
    return True
