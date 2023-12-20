import boto3
from botocore.exceptions import ClientError
from ..model.prayer_model import Prayer
import logging
import random
from decimal import Decimal

# logging
logger = logging.getLogger("gunicorn.error")

PRAYER_TABLE = "prayers"
PRAYER_TABLE_KEY = "PrayerCategory"
PRAYER_TABLE_SORT_KEY = "PrayerId"
REGION = "us-west-2"

dynamodb = boto3.resource("dynamodb", region_name="us-west-2")


def get_prayer(prayerCategory: str) -> Prayer:
    try:

        # Define the primary key value for the item you want to retrieve
        table = dynamodb.Table(PRAYER_TABLE)

        # Perform a get_item on the DynamoDB table
        response = table.get_item(Key={PRAYER_TABLE_KEY: prayerCategory})

        # Process the get_item response
        item = response.get("Item")
        if item:
            # Process the retrieved item as needed
            return Prayer(item["PrayerTitle"], item["PrayerText"])
        else:
            return Prayer("not_found", "not_found")
    except ClientError as e:
        # Handle the error
        error_code = e.response["Error"]["Code"]
        error_message = e.response["Error"]["Message"]
        logger.error(f"DynamoDB operation failed: {error_code} - {error_message}")
        return Prayer("error", "error")


def get_random_prayer() -> Prayer:
    try:
        # Define the primary key value for the item you want to retrieve
        table = dynamodb.Table(PRAYER_TABLE)

        # Generate a random number within the range of total items
        randId = Decimal(str(random.random()))

        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key(PRAYER_TABLE_KEY).eq(
                "Core"
            )
            & boto3.dynamodb.conditions.Key(PRAYER_TABLE_SORT_KEY).gt(randId),
            Limit=1,
        )

        if response["Items"]:
            # Process the retrieved item as needed
            prayer_item = response["Items"][0]
            return Prayer(prayer_item["PrayerTitle"], prayer_item["PrayerText"])
        else:
            response = table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key(
                    PRAYER_TABLE_KEY
                ).eq("Core")
                & boto3.dynamodb.conditions.Key(PRAYER_TABLE_SORT_KEY).lt(randId),
                ScanIndexForward=False,
                Limit=1,
            )
            prayer_item = response["Items"][0]
            return Prayer(prayer_item["PrayerTitle"], prayer_item["PrayerText"])
    except ClientError as e:
        # Handle the error
        error_code = e.response["Error"]["Code"]
        error_message = e.response["Error"]["Message"]
        logger.error(f"DynamoDB operation failed: {error_code} - {error_message}")
        # print(f"DynamoDB operation failed: {error_code} - {error_message}")
        return None
