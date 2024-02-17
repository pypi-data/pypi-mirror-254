variable "name" {
  description = "Prefix name to assign to Nebari resources"
  type        = string
}

variable "namespace" {
  description = "Namespace to create Kubernetes resources"
  type        = string
}

module "terraform-state" {
  source = "./modules/terraform-state"

  name = "${var.name}-${var.namespace}"

  tags = {
    Project     = var.name
    Owner       = "terraform-state"
    Environment = var.namespace
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.12.0"
    }
  }
  required_version = ">= 1.0"
}
