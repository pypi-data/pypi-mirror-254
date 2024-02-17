from typing import Any, Dict, List, Optional, Union
import os

from nebari.schema import Base
from _nebari.stages.base import NebariTerraformStage


class CertManagerCertificate(Base):
    name: str
    namespace: Optional[str] = None
    issuer: str


class CertManagerIssuer(Base):
    name: str
    namespace: Optional[str] = None
    type: Optional[str] = "letsencrypt"
    staging: Optional[bool] = False
    server: Optional[str] = None


class CertManagerAffinitySelectorConfig(Base):
    default: str


class CertManagerAffinityConfig(Base):
    enabled: Optional[bool] = True
    selector: Union[CertManagerAffinitySelectorConfig, str] = "general"

# email, certificates and issuers aren't really optional, but nebari
# validation blows up for init and any command that doesn't include
# a config file reference if I make them hard requirements
class CertManagerConfig(Base):
    name: Optional[str] = "cert-manager"
    namespace: Optional[str] = None
    affinity: CertManagerAffinityConfig = CertManagerAffinityConfig()
    email: Optional[str] = None
    solver: Optional[str] = "cloudflare"
    certificates: Optional[List[CertManagerCertificate]] = []
    issuers: Optional[List[CertManagerIssuer]] = []
    values: Optional[Dict[str, Any]] = {}


class InputSchema(Base):
    cert_manager: CertManagerConfig = CertManagerConfig()


class CertManagerStage(NebariTerraformStage):
    name = "cert-manager"
    priority = 100

    input_schema = InputSchema

    def input_vars(self, stage_outputs: Dict[str, Dict[str, Any]]):
        domain = stage_outputs["stages/04-kubernetes-ingress"]["domain"]
        zone = ".".join(domain.split(".")[-2:])

        chart_ns = self.config.cert_manager.namespace
        create_ns = True
        if chart_ns == None or chart_ns == "" or chart_ns == self.config.namespace:
            chart_ns = self.config.namespace
            create_ns = False

        for c in self.config.cert_manager.certificates:
            if c.namespace == None or len(c.namespace) == 0:
                c.namespace = self.config.namespace

        for i in self.config.cert_manager.issuers:
            if i.namespace == None or len(i.namespace) == 0:
                i.namespace = self.config.namespace

            if i.server == None or len(i.server) == 0:
                if i.type == "letsencrypt":
                    i.server = (
                        "https://acme-staging-v02.api.letsencrypt.org/directory"
                        if i.staging
                        else "https://acme-v02.api.letsencrypt.org/directory"
                    )

        return {
            "name": self.config.cert_manager.name,
            "domain": domain,
            "zone": zone,
            "create_namespace": create_ns,
            "namespace": chart_ns,
            "affinity": {
                "enabled": self.config.cert_manager.affinity.enabled,
                "selector": self.config.cert_manager.affinity.selector.__dict__
                if isinstance(self.config.cert_manager.affinity.selector, CertManagerAffinityConfig)
                else self.config.cert_manager.affinity.selector,
            },
            "email": self.config.cert_manager.email,
            "solver": self.config.cert_manager.solver,
            "certificates": [x.__dict__ for x in self.config.cert_manager.certificates],
            "apikey": os.environ["CLOUDFLARE_TOKEN"] if self.config.cert_manager.solver == "cloudflare" else "",
            "issuers": [x.__dict__ for x in self.config.cert_manager.issuers],
            "overrides": self.config.cert_manager.values,
        }
