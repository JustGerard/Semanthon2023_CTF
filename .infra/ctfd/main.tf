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
  source                = "1nval1dctf/ctfd/aws"
  https_certificate_arn = "arn:aws:acm:eu-north-1:995295403905:certificate/94e5d452-c6f6-4f46-8e83-ee0bcc21e7de"
  aws_region            = "eu-north-1"
  ctfd_image            = "public.ecr.aws/t1r2j1b6/ctf:latest"
}