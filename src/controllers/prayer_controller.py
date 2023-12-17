# /app/src/controllers/prayers_controller.py
from flask import Blueprint
import boto3

prayer_bp = Blueprint("prayer", __name__)


@prayer_bp.route("/prayer")
def get_prayer():
    dynamodb = boto3.resource("dynamodb")

    # Define the primary key value for the item you want to retrieve
    table_name = "prayers"
    table = dynamodb.Table(table_name)

    # Perform a get_item on the DynamoDB table
    response = table.get_item(Key={"PrayerTitle": "Saint Michael Prayer"})

    # Process the get_item response
    item = response.get("Item")
    if item:
        # Process the retrieved item as needed
        return f"Item: {item}"
    else:
        return "Item not found"
