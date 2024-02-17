variable "gpu_node_group_names" {
  description = "Names of node groups with GPU"
  default     = []
}

variable "gpu_enabled" {
  description = "Enable GPU support"
  default     = false
}

variable "cloud_provider" {
  description = "Name of cloud_provider"
  type        = string
}
