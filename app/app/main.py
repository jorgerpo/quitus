from fastapi import FastAPI
from starlette.requests import Request

from app.api.api_v1.api import api_router
from app.config import config
# from app.db.session import Session

app = FastAPI(
    title=config.PROJECT_TITLE, 
    description=config.PROJECT_DESC,
    version=config.PROJECT_VERSION,
    openapi_url=config.OPENAPI_JSON)

app.include_router(api_router, prefix=config.API_V1_STR)

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     request.state.db = Session()
#     response = await call_next(request)
#     request.state.db.close()
#     return response