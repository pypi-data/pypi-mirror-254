import json
from pathlib import Path
from unittest.mock import patch

from django.test import TestCase, override_settings

from openforms.authentication.constants import AuthAttribute
from openforms.plugins.exceptions import InvalidPluginConfiguration
from openforms.submissions.tests.factories import SubmissionFactory
from requests_mock import Mocker
from zgw_consumers.constants import APITypes
from zgw_consumers.test.factories import ServiceFactory

from ..models import HaalCentraalHRConfig
from ..plugin import HaalCentraalHRPrefill

FILES_DIR = Path(__file__).parent / "files"


@override_settings(LANGUAGE_CODE="en")
class HaalCentraalHRPluginTests(TestCase):
    def test_submission_not_authenticated(self):
        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        submission = SubmissionFactory.create()

        data = plugin.get_prefill_values(submission, ["address"])

        self.assertEqual(data, {})

    def test_submission_authenticated_with_other_auth_attribute(self):
        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        submission = SubmissionFactory.create(auth_info__attribute=AuthAttribute.bsn)

        data = plugin.get_prefill_values(submission, ["address"])

        self.assertEqual(data, {})

    def test_no_service_configured(self):
        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        submission = SubmissionFactory.create(
            auth_info__attribute=AuthAttribute.kvk, auth_info__value="111222333"
        )

        with patch(
            "prefill_haalcentraalhr.client.HaalCentraalHRConfig.get_solo",
            return_value=HaalCentraalHRConfig(),
        ):
            data = plugin.get_prefill_values(
                submission,
                ["kvkNummer", "heeftAlsEigenaar.natuurlijkPersoon.burgerservicenummer"],
            )

        self.assertEqual(data, {})

    @Mocker()
    @override_settings(ZGW_CONSUMERS_TEST_SCHEMA_DIRS=[FILES_DIR])
    def test_happy_flow(self, m):
        with open(FILES_DIR / "maatschappelijkeactiviteiten-response.json", "rb") as f:
            m.get(
                "http://haalcentraal-hr.nl/api/maatschappelijkeactiviteiten/111222333",
                json=json.load(f),
            )

        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        submission = SubmissionFactory.create(
            auth_info__attribute=AuthAttribute.kvk, auth_info__value="111222333"
        )
        service = ServiceFactory.create(
            api_type=APITypes.orc,
            api_root="http://haalcentraal-hr.nl/api/",
            oas="https://haalcentraal-hr.nl/api/schema/openapi.yaml",
        )

        with patch(
            "prefill_haalcentraalhr.client.HaalCentraalHRConfig.get_solo",
            return_value=HaalCentraalHRConfig(service=service),
        ):
            data = plugin.get_prefill_values(
                submission,
                ["kvkNummer", "heeftAlsEigenaar.natuurlijkPersoon.burgerservicenummer"],
            )

        self.assertEqual(data["kvkNummer"], "111222333")
        self.assertEqual(
            data["heeftAlsEigenaar.natuurlijkPersoon.burgerservicenummer"],
            "555555021",
        )

    @Mocker()
    @override_settings(ZGW_CONSUMERS_TEST_SCHEMA_DIRS=[FILES_DIR])
    def test_check_config_happy_flow(self, m):
        m.get(
            "http://haalcentraal-hr.nl/api/maatschappelijkeactiviteiten/TEST",
            status_code=400,
            json={
                "status": 400,
                "invalidParams": [
                    {"name": "kvkNummer", "reason": "Invalid KVK number."}
                ],
            },
        )

        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        service = ServiceFactory.create(
            api_type=APITypes.orc,
            api_root="http://haalcentraal-hr.nl/api/",
            oas="https://haalcentraal-hr.nl/api/schema/openapi.yaml",
        )

        with patch(
            "prefill_haalcentraalhr.client.HaalCentraalHRConfig.get_solo",
            return_value=HaalCentraalHRConfig(service=service),
        ):
            plugin.check_config()

    @Mocker()
    @override_settings(ZGW_CONSUMERS_TEST_SCHEMA_DIRS=[FILES_DIR])
    def test_check_config_wrong_response(self, m):
        m.get(
            "http://haalcentraal-hr.nl/api/maatschappelijkeactiviteiten/TEST",
            status_code=403,
            json={"status": 403, "title": "Not authorised!", "detail": "Error"},
        )

        plugin = HaalCentraalHRPrefill("haalcentraal_hr")
        service = ServiceFactory.create(
            api_type=APITypes.orc,
            api_root="http://haalcentraal-hr.nl/api/",
            oas="https://haalcentraal-hr.nl/api/schema/openapi.yaml",
        )

        with patch(
            "prefill_haalcentraalhr.client.HaalCentraalHRConfig.get_solo",
            return_value=HaalCentraalHRConfig(service=service),
        ):
            with self.assertRaises(
                InvalidPluginConfiguration,
                msg="Client error: {'status': 403, 'title': 'Not authorised!', 'detail': 'Error'}",
            ):
                plugin.check_config()

    def test_check_config_no_service_configured(self):
        plugin = HaalCentraalHRPrefill("haalcentraal_hr")

        with patch(
            "prefill_haalcentraalhr.client.HaalCentraalHRConfig.get_solo",
            return_value=HaalCentraalHRConfig(),
        ):
            with self.assertRaises(
                InvalidPluginConfiguration, msg="Service not selected"
            ):
                plugin.check_config()
