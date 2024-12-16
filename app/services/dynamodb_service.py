from app.services.aws_session import get_aioboto3_session

from app.config import DYNAMODB_TABLE_NAME


async def log_to_dynamodb(city: str, timestamp: str, file_url: str):
    session = get_aioboto3_session()
    async with session.client("dynamodb") as dynamodb:
        await dynamodb.put_item(
            TableName=DYNAMODB_TABLE_NAME,
            Item={
                "city": {"S": city},
                "timestamp": {"S": timestamp},
                "file_url": {"S": file_url}
            }
        )
