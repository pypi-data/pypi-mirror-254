# Shipped in Open Forms
from openforms.contrib.hal_client import HALClient
from openforms.pre_requests.clients import PreRequestMixin
from zgw_consumers.client import build_client

from .models import HaalCentraalHRConfig


class NoServiceConfigured(RuntimeError):
    pass


def get_client(**kwargs) -> "Client":
    config = HaalCentraalHRConfig.get_solo()
    assert isinstance(config, HaalCentraalHRConfig)
    if not (service := config.service):
        raise NoServiceConfigured("No service configured!")
    return build_client(service, client_factory=Client, **kwargs)


class Client(PreRequestMixin, HALClient):
    pass
