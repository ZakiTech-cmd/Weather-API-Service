import json
from datetime import datetime

from app.services.aws_session import get_aioboto3_session
from app.config import S3_BUCKET_NAME, AWS_REGION


async def save_to_s3(city: str, data: dict) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{city}_{timestamp}.json"
    json_data = json.dumps(data)

    session = get_aioboto3_session()
    async with session.client("s3") as s3_client:
        await s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=filename,
            Body=json_data
        )

    file_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{filename}"
    return file_url
