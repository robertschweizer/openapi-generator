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

from petstore_client.models.test_inline_freeform_additional_properties_request import TestInlineFreeformAdditionalPropertiesRequest

class TestTestInlineFreeformAdditionalPropertiesRequest(unittest.TestCase):
    """TestInlineFreeformAdditionalPropertiesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestInlineFreeformAdditionalPropertiesRequest:
        """Test TestInlineFreeformAdditionalPropertiesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestInlineFreeformAdditionalPropertiesRequest`
        """
        model = TestInlineFreeformAdditionalPropertiesRequest()
        if include_optional:
            return TestInlineFreeformAdditionalPropertiesRequest(
                some_property = ''
            )
        else:
            return TestInlineFreeformAdditionalPropertiesRequest(
        )
        """

    def testTestInlineFreeformAdditionalPropertiesRequest(self):
        """Test TestInlineFreeformAdditionalPropertiesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
