# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import petstore_client_aiohttp
from petstore_client_aiohttp.models.one_of_enum_string import OneOfEnumString  # noqa: E501
from petstore_client_aiohttp.rest import ApiException

class TestOneOfEnumString(unittest.TestCase):
    """OneOfEnumString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OneOfEnumString
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OneOfEnumString`
        """
        model = petstore_client_aiohttp.models.one_of_enum_string.OneOfEnumString()  # noqa: E501
        if include_optional :
            return OneOfEnumString(
            )
        else :
            return OneOfEnumString(
        )
        """

    def testOneOfEnumString(self):
        """Test OneOfEnumString"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
