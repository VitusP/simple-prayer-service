########################################################################################################################
## Create VPC with a CIDR block that has enough capacity for the amount of DNS names you need
########################################################################################################################

resource "aws_vpc" "default" {
  cidr_block           = var.vpc_cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name     = "${var.namespace}-VPC-${var.environment}"
    Scenario = var.scenario
  }
}

########################################################################################################################
## Create Internet Gateway for egress/ingress connections to resources in the public subnets
########################################################################################################################

resource "aws_internet_gateway" "default" {
  vpc_id = aws_vpc.default.id

  tags = {
    Name     = "${var.namespace}-InternetGateway-${var.environment}"
    Scenario = var.scenario
  }
}