# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import absolute_import

import unittest
import datetime

import petstore_client
from petstore_client.models.second_ref import SecondRef  # noqa: E501
from petstore_client.rest import ApiException

class TestSecondRef(unittest.TestCase):
    """SecondRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SecondRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecondRef`
        """
        model = petstore_client.models.second_ref.SecondRef()  # noqa: E501
        if include_optional :
            return SecondRef(
                category = '', 
                circular_ref = petstore_client.models.circular_reference_model.Circular-Reference-Model(
                    size = 56, 
                    nested = petstore_client.models.first_ref.FirstRef(
                        category = '', 
                        self_ref = petstore_client.models.second_ref.SecondRef(
                            category = '', ), ), )
            )
        else :
            return SecondRef(
        )
        """

    def testSecondRef(self):
        """Test SecondRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
