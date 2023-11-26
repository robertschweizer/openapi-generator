# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import petstore_client
from petstore_client.models.category import Category  # noqa: E501
from petstore_client.rest import ApiException

class TestCategory(unittest.TestCase):
    """Category unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Category
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = petstore_client.models.category.Category()  # noqa: E501
        if include_optional :
            return Category(
                id = 56, 
                name = 'default-name'
            )
        else :
            return Category(
                name = 'default-name',
        )

    def testCategory(self):
        """Test Category"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
