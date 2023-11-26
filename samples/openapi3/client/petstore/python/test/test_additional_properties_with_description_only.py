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

import petstore_client
from petstore_client.models.additional_properties_with_description_only import AdditionalPropertiesWithDescriptionOnly  # noqa: E501
from petstore_client.rest import ApiException

class TestAdditionalPropertiesWithDescriptionOnly(unittest.TestCase):
    """AdditionalPropertiesWithDescriptionOnly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdditionalPropertiesWithDescriptionOnly
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdditionalPropertiesWithDescriptionOnly`
        """
        model = petstore_client.models.additional_properties_with_description_only.AdditionalPropertiesWithDescriptionOnly()  # noqa: E501
        if include_optional :
            return AdditionalPropertiesWithDescriptionOnly(
                name = ''
            )
        else :
            return AdditionalPropertiesWithDescriptionOnly(
        )
        """

    def testAdditionalPropertiesWithDescriptionOnly(self):
        """Test AdditionalPropertiesWithDescriptionOnly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
