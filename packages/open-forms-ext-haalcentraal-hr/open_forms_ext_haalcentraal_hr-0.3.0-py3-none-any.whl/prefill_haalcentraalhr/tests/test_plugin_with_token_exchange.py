import json
from dataclasses import dataclass
from pathlib import Path
from unittest.mock import patch

from django.core.cache import cache
from django.test import TestCase, override_settings

from openforms.authentication.constants import AuthAttribute
from openforms.pre_requests.base import PreRequestHookBase
from openforms.pre_requests.registry import Registry
from openforms.submissions.models import Submission
from openforms.submissions.tests.factories import SubmissionFactory
from requests.auth import AuthBase
from requests_mock import Mocker
from zgw_consumers.constants import APITypes
from zgw_consumers.test.factories import ServiceFactory

from ..models import HaalCentraalHRConfig
from ..plugin import HaalCentraalHRPrefill

FILES_DIR = Path(__file__).parent / "files"

register = Registry()


@dataclass
class TestAuth(AuthBase):
    submission: Submission

    def __call__(self, request):
        request.headers["Authorization"] = "EXCHANGED TOKEN VALUE"
        return request


@register("token-exchange-test")
class TokenExchangePreRequestHookTest(PreRequestHookBase):
    def __call__(
        self,
        method,
        url,
        kwargs,
        context,
    ):
        kwargs["auth"] = TestAuth(submission=context["submission"])
        return


@Mocker()
@override_settings(ZGW_CONSUMERS_TEST_SCHEMA_DIRS=[FILES_DIR])
class HaalCentraalHRPluginWithTokenExchangeTests(TestCase):
    def test_token_exchange(self, m):
        with open(FILES_DIR / "maatschappelijkeactiviteiten-response.json", "rb") as f:
            m.get(
                "http://haalcentraal-hr.nl/api/maatschappelijkeactiviteiten/111222333",
                json=json.load(f),
            )

        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        submission = SubmissionFactory.create(
            auth_info__attribute=AuthAttribute.kvk,
            auth_info__value="111222333",
            auth_info__plugin="eherkenning_oidc",
        )
        cache.set(
            key=f"accesstoken:{submission.uuid}",
            value="ACCESS TOKEN VALUE",
        )

        service = ServiceFactory.create(
            api_type=APITypes.orc,
            api_root="http://haalcentraal-hr.nl/api/",
            oas="https://haalcentraal-hr.nl/api/schema/openapi.yaml",
        )

        with patch(
            "prefill_haalcentraalhr.client.HaalCentraalHRConfig.get_solo",
            return_value=HaalCentraalHRConfig(service=service),
        ), patch(
            "openforms.pre_requests.clients.registry",
            new=register,
        ):
            data = plugin.get_prefill_values(
                submission,
                ["kvkNummer", "heeftAlsEigenaar.natuurlijkPersoon.burgerservicenummer"],
            )

        self.assertEqual(data["kvkNummer"], "111222333")

        request_haalcentraal_headers = m.request_history[-1].headers

        self.assertIn("Authorization", request_haalcentraal_headers)
        self.assertEqual(
            request_haalcentraal_headers["Authorization"], "EXCHANGED TOKEN VALUE"
        )
