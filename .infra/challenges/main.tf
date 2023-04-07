terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.52.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

module "i_cant_feel_your_get" {
  source             = "./ecs"
  name               = "i-cant-feel-your-get"
  image              = "995295403905.dkr.ecr.eu-north-1.amazonaws.com/cant-feel-my-get:latest"
  execution_role_arn = local.execution_role_arn
  vpc_id             = local.vpc_id
  cluster_id         = local.cluster_id
  security_group_id  = local.security_group_id
  private_subnet_ids = local.private_subnet_ids
  cluster_name       = local.cluster_name
}
