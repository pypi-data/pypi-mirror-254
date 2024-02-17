locals {
  name             = var.name
  domain           = var.domain
  zone             = var.zone
  create_namespace = var.create_namespace
  namespace        = var.namespace
  email            = var.email
  solver           = var.solver
  certificates     = var.certificates
  apikey           = var.apikey
  issuers          = var.issuers
  overrides        = var.overrides

  affinity = var.affinity != null && lookup(var.affinity, "enabled", false) ? {
    enabled = true
    selector = try(
      { for k in ["default"] : k => length(var.affinity.selector[k]) > 0 ? var.affinity.selector[k] : var.affinity.selector.default },
      {
        default = var.affinity.selector
      },
    )
    } : {
    enabled  = false
    selector = null
  }

  chart_namespace = local.create_namespace ? kubernetes_namespace.this[0].metadata[0].name : local.namespace
}

resource "kubernetes_namespace" "this" {
  count = local.create_namespace ? 1 : 0

  metadata {
    name = local.namespace
  }
}

resource "kubernetes_secret" "cloudflare-apikey" {
  for_each = local.solver == "cloudflare" ? toset(distinct([for i in local.issuers : i.namespace])) : []

  metadata {
    name      = "${local.name}-cloudflare-apikey"
    namespace = each.value
  }

  data = {
    key = local.apikey
  }
}

resource "helm_release" "cert_manager" {
  name      = local.name
  namespace = local.chart_namespace

  repository = "https://charts.jetstack.io"
  chart      = "cert-manager"
  version    = "v1.11.1"

  values = [
    yamlencode({
      installCRDs = true
      affinity = local.affinity.enabled ? {
        nodeAffinity = {
          requiredDuringSchedulingIgnoredDuringExecution = {
            nodeSelectorTerms = [
              {
                matchExpressions = [
                  {
                    key      = "eks.amazonaws.com/nodegroup"
                    operator = "In"
                    values   = [local.affinity.selector.default]
                  }
                ]
              }
            ]
          }
        }
      } : {}
    }),
    yamlencode(lookup(local.overrides, "cert-manager", {})),
  ]
}

resource "helm_release" "certs" {
  name      = "${local.name}-certs"
  chart     = "./chart"
  namespace = local.chart_namespace

  values = [
    yamlencode({
      certificates = [
        for certificate in local.certificates : {
          name      = certificate.name
          namespace = certificate.namespace
          issuer    = certificate.issuer
          dnsNames  = [local.domain, "*.${local.domain}"]
        }
      ]
      issuers = [
        for issuer in local.issuers : {
          name      = issuer.name
          namespace = issuer.namespace
          type      = issuer.type
          server    = issuer.server
          email     = local.email
          solver = {
            type           = local.solver
            existingSecret = local.solver == "cloudflare" ? kubernetes_secret.cloudflare-apikey[issuer.namespace].metadata[0].name : ""
          }
        }
      ]
      cloudflare = {
        zone  = local.zone
        email = local.email
      }
    }),
    yamlencode(local.overrides),
  ]

  depends_on = [
    helm_release.cert_manager,
  ]
}
