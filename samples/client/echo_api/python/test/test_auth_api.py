# coding: utf-8

"""
    Echo Server API

    Echo Server API

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from echo_client.api.auth_api import AuthApi


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthApi()

    def tearDown(self) -> None:
        pass

    def test_test_auth_http_basic(self) -> None:
        """Test case for test_auth_http_basic

        To test HTTP basic authentication
        """
        pass

    def test_test_auth_http_bearer(self) -> None:
        """Test case for test_auth_http_bearer

        To test HTTP bearer authentication
        """
        pass


if __name__ == '__main__':
    unittest.main()
