from datetime import datetime

from fastapi import Query, APIRouter
from fastapi.responses import JSONResponse

from app.services.s3_service import save_to_s3
from app.services.dynamodb_service import log_to_dynamodb
from app.services.weather_service import fetch_weather_from_api
from app.utils.cache_utils import get_cached_weather

weather_router = APIRouter()


@weather_router.get(
    "/weather",
    tags=["Weather"],
    description="Get weather forecast for the city",
)
async def get_weather(city: str = Query(..., description="City name")):
    cached_data = await get_cached_weather(city)
    if cached_data:
        return JSONResponse(content={"weather_data": cached_data, "source": "cache"})

    weather_data = await fetch_weather_from_api(city)
    file_url = await save_to_s3(city, weather_data)

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    await log_to_dynamodb(city, timestamp, file_url)

    return JSONResponse(content={
        "weather_data": weather_data
    })
