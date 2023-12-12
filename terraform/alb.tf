########################################################################################################################
## Application Load Balancer in public subnets with HTTP default listener that redirects traffic to HTTPS
########################################################################################################################

resource "aws_alb" "alb" {
  name            = "${var.namespace}-ALB-${var.environment}"
  security_groups = [aws_security_group.alb.id]
  subnets         = aws_subnet.public.*.id

  tags = {
    Scenario = var.scenario
  }
}

########################################################################################################################
## Target Group for our service
########################################################################################################################

resource "aws_alb_target_group" "service_target_group" {
  name                 = "${var.namespace}-TargetGroup-${var.environment}"
  port                 = var.container_port
  protocol             = "HTTP"
  vpc_id               = aws_vpc.default.id
  deregistration_delay = 5
  target_type          = "ip"

  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    interval            = 60
    matcher             = var.healthcheck_matcher
    path                = var.healthcheck_endpoint
    port                = "traffic-port"
    protocol            = "HTTP"
    timeout             = 30
  }

  tags = {
    Scenario = var.scenario
  }

  depends_on = [aws_alb.alb]
}