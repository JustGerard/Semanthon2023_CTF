variable "name" {
  type = string
}

variable "image" {
  type = string
}

variable "execution_role_arn" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "cluster_id" {
  type = string
}

variable "security_group_id" {
  type = string
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "cluster_name" {
  type = string
}

variable "desired_count" {
  type    = number
  default = 2
}

variable "min_count" {
  type    = number
  default = 1
}

variable "max_count" {
  type    = number
  default = 4
}

variable "container_memory" {
  type    = number
  default = 1024
}

variable "container_cpu" {
  type    = number
  default = 512
}

variable "container_port" {
  type    = number
  default = 8000
}