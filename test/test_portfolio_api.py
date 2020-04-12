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
from ib_web_api.api.portfolio_api import PortfolioApi  # noqa: E501
from ib_web_api.rest import ApiException


class TestPortfolioApi(unittest.TestCase):
    """PortfolioApi unit test stubs"""

    def setUp(self):
        self.api = ib_web_api.api.portfolio_api.PortfolioApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_portfolio_account_id_allocation_get(self):
        """Test case for portfolio_account_id_allocation_get

        Account Allocation  # noqa: E501
        """
        pass

    def test_portfolio_account_id_ledger_get(self):
        """Test case for portfolio_account_id_ledger_get

        Account Ledger  # noqa: E501
        """
        pass

    def test_portfolio_account_id_meta_get(self):
        """Test case for portfolio_account_id_meta_get

        Account Information  # noqa: E501
        """
        pass

    def test_portfolio_account_id_position_conid_get(self):
        """Test case for portfolio_account_id_position_conid_get

        Position by Conid  # noqa: E501
        """
        pass

    def test_portfolio_account_id_positions_invalidate_post(self):
        """Test case for portfolio_account_id_positions_invalidate_post

        Invalidates the backend cache of the Portfolio  # noqa: E501
        """
        pass

    def test_portfolio_account_id_positions_page_id_get(self):
        """Test case for portfolio_account_id_positions_page_id_get

        Portfolio Positions  # noqa: E501
        """
        pass

    def test_portfolio_account_id_summary_get(self):
        """Test case for portfolio_account_id_summary_get

        Account Summary  # noqa: E501
        """
        pass

    def test_portfolio_accounts_get(self):
        """Test case for portfolio_accounts_get

        Portfolio Accounts  # noqa: E501
        """
        pass

    def test_portfolio_allocation_post(self):
        """Test case for portfolio_allocation_post

        Account Alloction (All Accounts)  # noqa: E501
        """
        pass

    def test_portfolio_positions_conid_get(self):
        """Test case for portfolio_positions_conid_get

        Positions by Conid  # noqa: E501
        """
        pass

    def test_portfolio_subaccounts_get(self):
        """Test case for portfolio_subaccounts_get

        List of Sub-Accounts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()