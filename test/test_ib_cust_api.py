# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ib_web_api
from ib_web_api.api.ib_cust_api import IBCustApi  # noqa: E501
from ib_web_api.rest import ApiException


class TestIBCustApi(unittest.TestCase):
    """IBCustApi unit test stubs"""

    def setUp(self):
        self.api = ib_web_api.api.ib_cust_api.IBCustApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ibcust_entity_info_get(self):
        """Test case for ibcust_entity_info_get

        IBCust Entity Info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
