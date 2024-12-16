import json
from datetime import datetime

from app.config import AWS_REGION, S3_BUCKET_NAME, CACHE_EXPIRATION
from app.services.aws_session import get_aioboto3_session


async def get_cached_weather(city: str) -> dict | None:
    prefix = f"{city}_"
    session = get_aioboto3_session()

    async with session.client("s3", region_name=AWS_REGION) as s3:
        response = await s3.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=prefix)

        if "Contents" in response:
            for obj in response["Contents"]:
                if (datetime.utcnow() - obj["LastModified"].replace(tzinfo=None)) < CACHE_EXPIRATION:
                    file_key = obj["Key"]
                    s3_response = await s3.get_object(Bucket=S3_BUCKET_NAME, Key=file_key)
                    content = await s3_response["Body"].read()
                    return json.loads(content)
    return None
