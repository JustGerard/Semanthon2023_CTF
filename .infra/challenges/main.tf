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

module "character_creator" {
  source                   = "./ecs"
  name                     = "character-creator"
  image                    = "995295403905.dkr.ecr.eu-north-1.amazonaws.com/character-creator:latest"
  execution_role_arn       = local.execution_role_arn
  vpc_id                   = local.vpc_id
  cluster_id               = local.cluster_id
  security_group_id        = local.security_group_id
  private_subnet_ids       = local.private_subnet_ids
  cluster_name             = local.cluster_name
  readonly_root_filesystem = false
}

module "mr-human" {
  source                   = "./ecs"
  name                     = "mr-human"
  image                    = "995295403905.dkr.ecr.eu-north-1.amazonaws.com/mr-human:latest"
  execution_role_arn       = local.execution_role_arn
  vpc_id                   = local.vpc_id
  cluster_id               = local.cluster_id
  security_group_id        = local.security_group_id
  private_subnet_ids       = local.private_subnet_ids
  cluster_name             = local.cluster_name
  readonly_root_filesystem = false
}

module "my-gallery" {
  source                   = "./ecs"
  name                     = "my-gallery"
  image                    = "995295403905.dkr.ecr.eu-north-1.amazonaws.com/my-gallery:latest"
  execution_role_arn       = local.execution_role_arn
  vpc_id                   = local.vpc_id
  cluster_id               = local.cluster_id
  security_group_id        = local.security_group_id
  private_subnet_ids       = local.private_subnet_ids
  cluster_name             = local.cluster_name
  readonly_root_filesystem = false
  healthcheck              = "/images/"
}

module "simple-question" {
  source                   = "./ecs"
  name                     = "simple-question"
  image                    = "995295403905.dkr.ecr.eu-north-1.amazonaws.com/simple-question:latest"
  execution_role_arn       = local.execution_role_arn
  vpc_id                   = local.vpc_id
  cluster_id               = local.cluster_id
  security_group_id        = local.security_group_id
  private_subnet_ids       = local.private_subnet_ids
  cluster_name             = local.cluster_name
  readonly_root_filesystem = false
}