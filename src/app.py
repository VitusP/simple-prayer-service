# app/app.py
from flask import Flask
import boto3

app = Flask(__name__)


@app.route("/prayers")
def get_prayer():
    dynamodb = boto3.client("dynamodb")

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


@app.route("/")
def hello():
    return "simple-prayer-service in ECS!"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
