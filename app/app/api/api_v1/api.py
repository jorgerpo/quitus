from fastapi import APIRouter
  
from app.api.api_v1.endpoints import rule
api_router = APIRouter()
api_router.include_router(rule.router, prefix="/rule")
