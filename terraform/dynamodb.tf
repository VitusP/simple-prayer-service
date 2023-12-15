########################################################################################################################
## Create log group for our service
########################################################################################################################

resource "aws_dynamodb_table" "simple_prayer_service_prayers" {
  name         = "prayers"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "PrayerTitle"
  range_key    = "PrayerCategory"

  attribute {
    name = "PrayerTitle"
    type = "S"
  }

  attribute {
    name = "PrayerCategory"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  tags = {
    Name        = "simple-prayer-service-prayers-dynamodb"
    Environment = "production"
  }
}