data "aws_region" "current" {}

resource "aws_cloudwatch_log_group" "log_group" {
  name = var.name

  tags = {
    Environment = "production"
    Application = var.name
  }
}

module "container_definition" {
  source                   = "cloudposse/ecs-container-definition/aws"
  version                  = "0.58.1"
  container_name           = var.name
  container_image          = var.image
  container_memory         = var.container_memory
  container_cpu            = var.container_cpu
  readonly_root_filesystem = var.readonly_root_filesystem

  log_configuration = {
    logDriver = "awslogs"
    options = {
      awslogs-group         = aws_cloudwatch_log_group.log_group.name
      awslogs-region        = data.aws_region.current.name
      awslogs-stream-prefix = var.name
    }
  }
  port_mappings = [
    {
      containerPort = var.container_port
      hostPort      = var.container_port
      protocol      = "tcp"
    }
  ]
}

resource "aws_ecs_task_definition" "task_definition" {
  family                   = var.name
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = var.container_cpu
  memory                   = var.container_memory
  execution_role_arn       = var.execution_role_arn
  container_definitions    = module.container_definition.json_map_encoded_list
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }
}

resource "aws_lb_target_group" "target_group" {
  port        = var.container_port
  protocol    = "HTTP"
  vpc_id      = var.vpc_id
  target_type = "ip"
  health_check {
    path = var.healthcheck
  }
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_ecs_service" "ecs_service" {
  name            = var.name
  cluster         = var.cluster_id
  task_definition = aws_ecs_task_definition.task_definition.arn
  launch_type     = "FARGATE"

  desired_count                      = var.desired_count
  deployment_minimum_healthy_percent = 75
  deployment_maximum_percent         = 150

  load_balancer {
    target_group_arn = aws_lb_target_group.target_group.arn
    container_name   = var.name
    container_port   = var.container_port
  }
  network_configuration {

    security_groups = [var.security_group_id]
    subnets         = var.private_subnet_ids
  }
}

resource "aws_appautoscaling_target" "autoscaling_target" {
  max_capacity       = var.max_count
  min_capacity       = var.min_count
  resource_id        = "service/${var.cluster_name}/${aws_ecs_service.ecs_service.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}