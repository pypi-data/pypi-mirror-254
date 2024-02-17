variable "name" {
  type = string
}

variable "domain" {
  type = string
}

variable "zone" {
  type = string
}

variable "create_namespace" {
  type = bool
}

variable "namespace" {
  type = string
}

variable "email" {
  type = string
}

variable "solver" {
  type = string
}

variable "certificates" {
  type = list(object({
    name      = string
    namespace = string
    issuer    = string
  }))
}

variable "apikey" {
  type = string
}

variable "issuers" {
  type = list(object({
    name      = string
    namespace = string
    type      = string
    server    = string
    staging   = optional(bool, false)
  }))
}

variable "overrides" {
  type    = any
  default = {}
}

variable "affinity" {
  type = object({
    enabled  = optional(bool, true)
    selector = optional(any, "general")
  })

  default = {
    enabled  = false
    selector = "general"
  }

  validation {
    condition     = can(tostring(var.affinity.selector)) || (can(var.affinity.selector.default) && length(try(var.affinity.selector.default, "")) > 0)
    error_message = "\"affinity.selector\" argument must be a string or object { default }"
  }
}
