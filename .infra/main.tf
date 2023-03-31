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

module "ctfd" {
  source     = "1nval1dctf/ctfd/aws"
  aws_region = "eu-north-1"
  ctfd_image = "public.ecr.aws/t1r2j1b6/my-ctfd:latest"
}