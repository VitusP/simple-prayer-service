########################################################################################################################
## IAM Role for ECS Task execution
########################################################################################################################

resource "aws_iam_role" "ecs_task_execution_role" {
  name               = "${var.namespace}-ECS-TaskExecutionRole-${var.environment}"
  assume_role_policy = data.aws_iam_policy_document.task_assume_role_policy.json

  tags = {
    Scenario = var.scenario
  }
}

data "aws_iam_policy_document" "task_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

########################################################################################################################
## IAM Role for ECS Task
########################################################################################################################

resource "aws_iam_role" "ecs_task_iam_role" {
  name               = "${var.namespace}-ECS-TaskIAMRole-${var.environment}"
  assume_role_policy = data.aws_iam_policy_document.task_assume_role_policy.json

  tags = {
    Scenario = var.scenario
  }
}

########################################################################################################################
## IAM Policies for dynamodb
########################################################################################################################

data "aws_iam_policy_document" "dynamodb_policy" {
  statement {
    sid = "DynamodbPolicy"
    actions = [
      "dynamodb:BatchGetItem",
      "dynamodb:GetItem",
      "dynamodb:Query",
      "dynamodb:Scan",
      "dynamodb:BatchWriteItem",
      "dynamodb:PutItem",
      "dynamodb:UpdateItem",
      "dynamodb:DeleteItem"
    ]

    resources = [
      aws_dynamodb_table.simple_prayer_service_prayers.arn
    ]
  }
}

resource "aws_iam_policy" "dynamodb_policy" {
  name   = "${var.namespace}-Dynamodb-TaskPolicy-${var.environment}"
  policy = data.aws_iam_policy_document.dynamodb_policy.json
}

resource "aws_iam_role_policy_attachment" "dynamodb_policy" {
  role       = aws_iam_role.ecs_task_iam_role.name
  policy_arn = aws_iam_policy.dynamodb_policy.arn
}