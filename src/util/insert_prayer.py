import boto3
import random
from decimal import Decimal

PRAYER_TABLE = "prayers"
PRAYER_TABLE_KEY = "PrayerCategory"
PRAYER_TABLE_SORT_KEY = "PrayerId"
REGION = "us-west-2"
PRAYER_CATEGORY = "Core"
PRAYER_TITLE = "Miraculous Medal Prayer"
PRAYER_TEXT = "O Mary, Conceived without Sin, pray for us who have recourse to thee, and for those who do not have recourse to thee, especially the enemies of the Church. Amen."
dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
table = dynamodb.Table(PRAYER_TABLE)

randId = Decimal(str(random.random()))
item = {
    PRAYER_TABLE_KEY: PRAYER_CATEGORY,
    PRAYER_TABLE_SORT_KEY: randId,
    "PrayerTitle": PRAYER_TITLE,
    "PrayerText": PRAYER_TEXT,
}

table.put_item(Item=item)
