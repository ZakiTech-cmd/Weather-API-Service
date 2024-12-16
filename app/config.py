import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

# OpenWeatherMap API Key
API_KEY = os.getenv("API_KEY")

# Cache Expiration Time
CACHE_EXPIRATION = timedelta(minutes=int(os.getenv("CACHE_EXPIRATION_MINUTES", 5)))
