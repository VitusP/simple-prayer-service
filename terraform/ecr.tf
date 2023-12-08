resource "aws_ecr_repository" "simple_prayer_service_ecr" {
  name                 = "simple-prayer-service-ecr"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}