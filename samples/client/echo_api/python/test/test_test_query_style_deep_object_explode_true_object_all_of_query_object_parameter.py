# coding: utf-8

"""
    Echo Server API

    Echo Server API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import echo_client
from echo_client.models.test_query_style_deep_object_explode_true_object_all_of_query_object_parameter import TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter  # noqa: E501
from echo_client.rest import ApiException

class TestTestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter(unittest.TestCase):
    """TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter`
        """
        model = echo_client.models.test_query_style_deep_object_explode_true_object_all_of_query_object_parameter.TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter()  # noqa: E501
        if include_optional :
            return TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter(
                size = '', 
                color = '', 
                id = 1, 
                name = 'Dogs'
            )
        else :
            return TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter(
        )
        """

    def testTestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter(self):
        """Test TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
