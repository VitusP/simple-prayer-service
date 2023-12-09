terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30.0"
    }
  }

  required_version = ">= 1.2.0"
  backend "s3" {
    bucket = "simple-prayer-service-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-west-2"
  }
}

provider "aws" {
  region = "us-west-2"
}
