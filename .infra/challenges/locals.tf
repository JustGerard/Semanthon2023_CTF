locals {
  execution_role_arn = "arn:aws:iam::995295403905:role/ecs-staging-execution-role"
  vpc_id             = "vpc-09308c8b3c3614618"
  cluster_id         = "arn:aws:ecs:eu-north-1:995295403905:cluster/ctfd-ecs"
  security_group_id  = "sg-02ed40837a9ec6850"
  private_subnet_ids = ["subnet-0a4012c436b83d6b0", "subnet-024f4427881184f44", "subnet-0222b66fd37adb405"]
  cluster_name       = "ctfd-ecs"
}