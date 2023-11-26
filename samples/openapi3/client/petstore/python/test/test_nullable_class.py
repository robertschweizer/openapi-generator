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

from petstore_client.models.nullable_class import NullableClass

class TestNullableClass(unittest.TestCase):
    """NullableClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NullableClass:
        """Test NullableClass
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NullableClass`
        """
        model = NullableClass()
        if include_optional:
            return NullableClass(
                required_integer_prop = 56,
                integer_prop = 56,
                number_prop = 1.337,
                boolean_prop = True,
                string_prop = '',
                date_prop = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                datetime_prop = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                array_nullable_prop = [
                    None
                    ],
                array_and_items_nullable_prop = [
                    None
                    ],
                array_items_nullable = [
                    None
                    ],
                object_nullable_prop = {
                    'key' : None
                    },
                object_and_items_nullable_prop = {
                    'key' : None
                    },
                object_items_nullable = {
                    'key' : None
                    }
            )
        else:
            return NullableClass(
                required_integer_prop = 56,
        )
        """

    def testNullableClass(self):
        """Test NullableClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
