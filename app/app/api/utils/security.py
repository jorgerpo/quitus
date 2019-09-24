from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from app.config import config
from starlette.status import HTTP_403_FORBIDDEN

apikey_scheme = APIKeyHeader(name=config.APIKEY_HEADER_NAME)


def check_token(token: str = Security(apikey_scheme)):
    if token != config.APIKEY_HEADER_TOKEN:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Access Forbidden")
    return True
