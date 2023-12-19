import boto3
import random

PRAYER_TABLE = "prayers"
PRAYER_TABLE_KEY = "PrayerTitle"
PRAYER_TABLE_SORT_KEY = "PrayerId"
REGION = "us-west-2"
PRAYER_TITLE = "Prayer Title 1"
PRAYER_TEXT = "Test Sample Prayer"

dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
table = dynamodb.Table(PRAYER_TABLE)

randId = random.random()
item = {
    PRAYER_TABLE_KEY: PRAYER_TITLE,
    PRAYER_TABLE_SORT_KEY: randId,
    "PrayerText": PRAYER_TEXT,
}

table.put_item(Item=item)
