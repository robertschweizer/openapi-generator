# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import petstore_client_aiohttp
from petstore_client_aiohttp.api.another_fake_api import AnotherFakeApi  # noqa: E501
from petstore_client_aiohttp.rest import ApiException


class TestAnotherFakeApi(unittest.TestCase):
    """AnotherFakeApi unit test stubs"""

    def setUp(self):
        self.api = petstore_client_aiohttp.api.another_fake_api.AnotherFakeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_call_123_test_special_tags(self):
        """Test case for call_123_test_special_tags

        To test special tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
