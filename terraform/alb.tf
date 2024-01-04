########################################################################################################################
## Application Load Balancer in public subnets with HTTP default listener that redirects traffic to HTTP
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
## Default HTTP listener
########################################################################################################################

resource "aws_alb_listener" "alb_default_listener_http" {
  load_balancer_arn = aws_alb.alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type = "fixed-response"

    fixed_response {
      content_type = "text/plain"
      status_code  = "200"
      message_body = "OK"
    }
  }
}

########################################################################################################################
## HTTPS Listener Rule to only allow traffic with a valid custom origin header coming from CloudFront
########################################################################################################################

resource "aws_alb_listener_rule" "http_listener_rule" {
  listener_arn = aws_alb_listener.alb_default_listener_http.arn

  action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.service_target_group.arn
  }
  condition {
    path_pattern {
      values = ["/*"]
    }
  }
}

########################################################################################################################
## Target Group for our service
########################################################################################################################

resource "aws_alb_target_group" "service_target_group" {
  name                 = "${var.namespace}-tg-${var.environment}"
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

  # depends_on = [aws_alb.alb]
}
