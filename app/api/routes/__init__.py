from fastapi import APIRouter
from app.api.routes.weather_routes import weather_router

router = APIRouter()

router.include_router(weather_router)
