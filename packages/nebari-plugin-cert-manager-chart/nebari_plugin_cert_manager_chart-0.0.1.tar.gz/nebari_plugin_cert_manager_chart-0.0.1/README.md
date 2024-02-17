
# Nebari Plugin Cert-Manager Chart

[![PyPI - Version](https://img.shields.io/pypi/v/nebari-plugin-cert-manager-chart.svg)](https://pypi.org/project/nebari-plugin-cert-manager-chart)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nebari-plugin-cert-manager-chart.svg)](https://pypi.org/project/nebari-plugin-cert-manager-chart)

-----

## Overview
This plugin integrates cert-manager into the Nebari platform, allowing X.509 certificate management within Nebari. Utilizing Python, Terraform, Kubernetes, and Helm charts, the plugin provides a configurable deployment.

## Design and Architecture
The plugin follows a modular design, leveraging Terraform to define the deployment of cert-manager within a Kubernetes cluster. Key components include:
- **Terraform Configuration**: Defines variables, outputs, and resources for deployment, including Helm release and Kubernetes secrets.
- **Helm Chart Integration**: Deploys cert-manager as a Helm chart within the specified Kubernetes namespace.

## Installation Instructions


```console
pip install nebari-plugin-cert-manager-chart
```


## Usage Instructions
**Configurations**: Various configurations are available, including email, certificate, issuer, solver, and namespace settings.

## Configuration Details

### Environment Variable
The below environment variable must be present when deploying Nebari platform to create cloudflare-api Secret for Issuer to retrieve if using Cloudflare solver.

```bash
#### cloudflare-apikey

# have to get the client secret from cloudflare manually
export CLOUDFLARE_TOKEN="!!!GetThisFromCloudflareConsole!!!"
```

### Public
Configuration of the cert-manager plugin is controlled through the `cert_manager` section of the `nebari-config.yaml` for the environment.

``` yaml
cert_manager:
  # helm release name and namespace - default default (nebari global namespace)
  namespace: cert-manager
  # email address to be associated with the ACME account
  email: sblair@metrostar.com
  # API to manage DNS01 ACME challenge records - default cloudflare
  solver: cloudflare
  # whether to use ACME server's staging or production endpoint - default false
  staging: false
  # list of certificate resources to be created
  certificates:
    # name of certificate
  - name: metrostar-certificate
    # issuer responsible for issuing the certificate
    issuer: letsencrypt
  # list of issuers representing certificate issuing authority
  issuers:
    # name of issuer
  - name: letsencrypt
    # type of issuer
    type: letsencrypt
    # ID of the CA key that the External Account is bound to, if any - leave blank if none
    keyId: ""
    # symmetric MAC key of the External Account Binding, if any - leave blank if none
    existingSecret: ""
  # helm chart values overrides
  values: {}
```

### Internal
The following configuration values apply to the internally managed terraform module and are indirectly controlled through related values in `nebari-config.yaml`.

- `domain`, `zone`: Domain and zone for the plugin's deployment.
- `create_namespace`, `namespace`: Helm release's namespace configuration.
- `email`: Cloudflare email address.
- `solver`: Solver type.
- `staging`: Flag to use staging or production endpoint environment.
- `certificates`: cert-manager Certificate resources to be stored in Kubernetes Secret resources.
- `apikey`: Cloudflare API Token.
- `issuers`: cert-manager Issuer resources.
- `overrides`: Map for overriding default configurations.

## Testing Overview

The plugin includes unit tests to validate its core functionalities:

- **Constructor Test**: Verifies the default priority.
- **Input Variables Test**: Validates namespaces, solver type, staging flag.
- **Default Namespace Test**: Tests the default namespace configuration.

## License

`nebari-plugin-label-studio-chart` is distributed under the terms of the [Apache](./LICENSE.md) license.