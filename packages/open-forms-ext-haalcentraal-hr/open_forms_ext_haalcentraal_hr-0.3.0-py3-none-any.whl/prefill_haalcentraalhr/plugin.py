import logging

from django.utils.translation import gettext_lazy as _

import requests
from glom import GlomError, glom
from openforms.authentication.constants import AuthAttribute
from openforms.plugins.exceptions import InvalidPluginConfiguration
from openforms.pre_requests.clients import PreRequestClientContext
from openforms.prefill.base import BasePlugin
from openforms.prefill.constants import IdentifierRoles
from openforms.prefill.registry import register
from openforms.submissions.models import Submission
from openforms.typing import JSONObject
from zds_client import ClientError

from .client import NoServiceConfigured, get_client
from .constants import Attributes

logger = logging.getLogger(__name__)


@register("haalcentraal_hr")
class HaalCentraalHRPrefill(BasePlugin):
    verbose_name = _("Haal Centraal HR")
    requires_auth = AuthAttribute.kvk

    def get_available_attributes(self) -> list[tuple[str, str]]:
        return Attributes.choices

    def get_identifier_value(
        self, submission: Submission, identifier_role: str
    ) -> str | None:
        if not submission.is_authenticated:
            return

        if (
            identifier_role == IdentifierRoles.main
            and submission.auth_info.attribute == self.requires_auth
        ):
            return submission.auth_info.value

    def extract_requested_attributes(
        self, attributes: list[str], data: JSONObject | None
    ) -> JSONObject:
        if not data:
            return {}

        values = dict()
        for attr in attributes:
            try:
                values[attr] = glom(data, attr)
            except GlomError as exc:
                logger.warning(
                    "Missing expected attribute '%s' in Haal Centraal HR response",
                    attr,
                    exc_info=exc,
                )

        return values

    def get_prefill_values(
        self,
        submission: Submission,
        attributes: list[str],
        identifier_role: str = IdentifierRoles.main,
    ) -> JSONObject:
        # check if submission was logged in with the identifier we're interested
        if not (kvk_value := self.get_identifier_value(submission, identifier_role)):
            return {}

        context = PreRequestClientContext(submission=submission)
        try:
            haal_centraal_hr_client = get_client(context=context)
        except NoServiceConfigured:
            logger.exception("Haal Centraal HR service not configured.")
            return {}

        try:
            with haal_centraal_hr_client:
                response = haal_centraal_hr_client.get(
                    f"maatschappelijkeactiviteiten/{kvk_value}"
                )
                response.raise_for_status()
        except requests.RequestException as exc:
            logger.exception(
                "Exception while making request to Haal Centraal HR", exc_info=exc
            )
            return {}

        data = response.json()
        return self.extract_requested_attributes(attributes, data)

    def check_config(self) -> None:
        kvk_value = "TEST"
        try:
            with get_client() as client:
                response = client.get(f"maatschappelijkeactiviteiten/{kvk_value}")
                response.raise_for_status()
        except NoServiceConfigured as exc:
            raise InvalidPluginConfiguration(_("Service not selected")) from exc
        except requests.RequestException as exc:
            if (response := exc.response) is not None and response.status_code == 400:
                return
            raise InvalidPluginConfiguration(
                _("Client error: {exception}").format(exception=exc)
            ) from exc
