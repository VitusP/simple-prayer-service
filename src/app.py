# app/app.py
from flask import Flask
import boto3

app = Flask(__name__)

@app.route('/')
def hello():
    dynamodb = boto3.client('dynamodb')

    # Define the primary key value for the item you want to retrieve
    table_name = "prayers"
    primary_key = {
        'PrayerTitle': {'S': "Saint Michael Prayer"}
    }

    # Perform a get_item on the DynamoDB table
    response = dynamodb.get_item(
        TableName=table_name,
        Key=primary_key
    )

    # Process the get_item response
    item = response.get('Item')
    if item:
        # Process the retrieved item as needed
        return f"Item: {item}"
    else:
        return "Item not found"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)
