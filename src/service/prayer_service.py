import boto3
from botocore.exceptions import ClientError
from ..model.prayer_model import Prayer
import logging
import random

# logging
logger = logging.getLogger("gunicorn.error")

PRAYER_TABLE = "prayers"
PRAYER_TABLE_KEY = "PrayerTitle"
REGION = "us-west-2"


def get_prayer(prayerTitle: str) -> Prayer:
    try:
        dynamodb = boto3.resource("dynamodb")

        # Define the primary key value for the item you want to retrieve
        table = dynamodb.Table(PRAYER_TABLE)

        # Perform a get_item on the DynamoDB table
        response = table.get_item(Key={PRAYER_TABLE_KEY: prayerTitle})

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
        dynamodb = boto3.resource("dynamodb")

        # Define the primary key value for the item you want to retrieve
        table = dynamodb.Table(PRAYER_TABLE)

        # Generate a random number within the range of total items
        response = table.scan()
        items_list = response.get("Items", [])
        items_length = len(items_list)
        random_index = random.randint(0, items_length - 1)
        logger.info(f"Scanned {items_length} prayers in prayer table: {items_list}")

        # Process the get_item response
        item = items_list[random_index] if items_list[random_index] else None
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
        # print(f"DynamoDB operation failed: {error_code} - {error_message}")
        return None
