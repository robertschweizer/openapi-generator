# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_client.api.another_fake_api import AnotherFakeApi


class TestAnotherFakeApi(unittest.TestCase):
    """AnotherFakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnotherFakeApi()

    def tearDown(self) -> None:
        pass

    def test_call_123_test_special_tags(self) -> None:
        """Test case for call_123_test_special_tags

        To test special tags
        """
        pass


if __name__ == '__main__':
    unittest.main()
