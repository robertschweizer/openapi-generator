# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from petstore_client.models.array_of_number_only import ArrayOfNumberOnly

class TestArrayOfNumberOnly(unittest.TestCase):
    """ArrayOfNumberOnly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfNumberOnly:
        """Test ArrayOfNumberOnly
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfNumberOnly`
        """
        model = ArrayOfNumberOnly()
        if include_optional:
            return ArrayOfNumberOnly(
                array_number = [
                    1.337
                    ]
            )
        else:
            return ArrayOfNumberOnly(
        )
        """

    def testArrayOfNumberOnly(self):
        """Test ArrayOfNumberOnly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
