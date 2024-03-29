# ib-web-api
Production version of the Client Portal Web API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ib_web_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ib_web_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.AccountApi(ib_web_api.ApiClient(configuration))

try:
    # PnL for the selected account
    api_response = api_instance.iserver_account_pnl_partitioned_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->iserver_account_pnl_partitioned_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:5000/v1/portal*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**iserver_account_pnl_partitioned_get**](docs/AccountApi.md#iserver_account_pnl_partitioned_get) | **GET** /iserver/account/pnl/partitioned | PnL for the selected account
*AccountApi* | [**iserver_account_post**](docs/AccountApi.md#iserver_account_post) | **POST** /iserver/account | Updates currently selected account to the provided account
*AccountApi* | [**iserver_accounts_get**](docs/AccountApi.md#iserver_accounts_get) | **GET** /iserver/accounts | Brokerage Accounts
*AccountApi* | [**portfolio_account_id_ledger_get**](docs/AccountApi.md#portfolio_account_id_ledger_get) | **GET** /portfolio/{accountId}/ledger | Account Ledger
*AccountApi* | [**portfolio_account_id_meta_get**](docs/AccountApi.md#portfolio_account_id_meta_get) | **GET** /portfolio/{accountId}/meta | Account Information
*AccountApi* | [**portfolio_account_id_summary_get**](docs/AccountApi.md#portfolio_account_id_summary_get) | **GET** /portfolio/{accountId}/summary | Account Summary
*AccountApi* | [**portfolio_accounts_get**](docs/AccountApi.md#portfolio_accounts_get) | **GET** /portfolio/accounts | Portfolio Accounts
*AccountApi* | [**portfolio_subaccounts_get**](docs/AccountApi.md#portfolio_subaccounts_get) | **GET** /portfolio/subaccounts | List of Sub-Accounts
*ContractApi* | [**iserver_contract_conid_info_get**](docs/ContractApi.md#iserver_contract_conid_info_get) | **GET** /iserver/contract/{conid}/info | Contract Info
*ContractApi* | [**iserver_secdef_search_post**](docs/ContractApi.md#iserver_secdef_search_post) | **POST** /iserver/secdef/search | Search by symbol or name
*ContractApi* | [**trsrv_futures_get**](docs/ContractApi.md#trsrv_futures_get) | **GET** /trsrv/futures | Security Futures by Symbol
*ContractApi* | [**trsrv_secdef_post**](docs/ContractApi.md#trsrv_secdef_post) | **POST** /trsrv/secdef | Secdef by Conid
*FYIApi* | [**fyi_deliveryoptions_device_id_delete**](docs/FYIApi.md#fyi_deliveryoptions_device_id_delete) | **DELETE** /fyi/deliveryoptions/{deviceId} | delete a device
*FYIApi* | [**fyi_deliveryoptions_device_post**](docs/FYIApi.md#fyi_deliveryoptions_device_post) | **POST** /fyi/deliveryoptions/device | enable/disable device option
*FYIApi* | [**fyi_deliveryoptions_email_put**](docs/FYIApi.md#fyi_deliveryoptions_email_put) | **PUT** /fyi/deliveryoptions/email | enable/disable email option
*FYIApi* | [**fyi_deliveryoptions_get**](docs/FYIApi.md#fyi_deliveryoptions_get) | **GET** /fyi/deliveryoptions | Get delivery options
*FYIApi* | [**fyi_disclaimer_typecode_get**](docs/FYIApi.md#fyi_disclaimer_typecode_get) | **GET** /fyi/disclaimer/{typecode} | get disclaimer for a certain kind of fyi
*FYIApi* | [**fyi_disclaimer_typecode_put**](docs/FYIApi.md#fyi_disclaimer_typecode_put) | **PUT** /fyi/disclaimer/{typecode} | mark disclaimer read
*FYIApi* | [**fyi_notifications_get**](docs/FYIApi.md#fyi_notifications_get) | **GET** /fyi/notifications | Get a list of notifications
*FYIApi* | [**fyi_notifications_more_get**](docs/FYIApi.md#fyi_notifications_more_get) | **GET** /fyi/notifications/more | Get more notifications based on a certain one
*FYIApi* | [**fyi_notifications_notification_id_put**](docs/FYIApi.md#fyi_notifications_notification_id_put) | **PUT** /fyi/notifications/{notificationId} | Get a list of notifications
*FYIApi* | [**fyi_settings_get**](docs/FYIApi.md#fyi_settings_get) | **GET** /fyi/settings | Get a list of subscriptions
*FYIApi* | [**fyi_settings_typecode_post**](docs/FYIApi.md#fyi_settings_typecode_post) | **POST** /fyi/settings/{typecode} | enable/disable certain subscription
*FYIApi* | [**fyi_unreadnumber_get**](docs/FYIApi.md#fyi_unreadnumber_get) | **GET** /fyi/unreadnumber | Get unread number of fyis
*IBCustApi* | [**ibcust_entity_info_get**](docs/IBCustApi.md#ibcust_entity_info_get) | **GET** /ibcust/entity/info | IBCust Entity Info
*MarketDataApi* | [**iserver_marketdata_history_get**](docs/MarketDataApi.md#iserver_marketdata_history_get) | **GET** /iserver/marketdata/history | Market Data History
*MarketDataApi* | [**iserver_marketdata_snapshot_get**](docs/MarketDataApi.md#iserver_marketdata_snapshot_get) | **GET** /iserver/marketdata/snapshot | Market Data
*OrderApi* | [**iserver_account_account_id_order_orig_customer_order_id_delete**](docs/OrderApi.md#iserver_account_account_id_order_orig_customer_order_id_delete) | **DELETE** /iserver/account/{accountId}/order/{origCustomerOrderId} | Delete Order
*OrderApi* | [**iserver_account_account_id_order_orig_customer_order_id_post**](docs/OrderApi.md#iserver_account_account_id_order_orig_customer_order_id_post) | **POST** /iserver/account/{accountId}/order/{origCustomerOrderId} | Modify Order
*OrderApi* | [**iserver_account_account_id_order_post**](docs/OrderApi.md#iserver_account_account_id_order_post) | **POST** /iserver/account/{accountId}/order | Place Order
*OrderApi* | [**iserver_account_account_id_order_whatif_post**](docs/OrderApi.md#iserver_account_account_id_order_whatif_post) | **POST** /iserver/account/{accountId}/order/whatif | Preview Order
*OrderApi* | [**iserver_account_account_id_orders_post**](docs/OrderApi.md#iserver_account_account_id_orders_post) | **POST** /iserver/account/{accountId}/orders | Place Orders (Support bracket orders)
*OrderApi* | [**iserver_account_orders_get**](docs/OrderApi.md#iserver_account_orders_get) | **GET** /iserver/account/orders | Live Orders
*OrderApi* | [**iserver_reply_replyid_post**](docs/OrderApi.md#iserver_reply_replyid_post) | **POST** /iserver/reply/{replyid} | Place Order Reply
*PnLApi* | [**iserver_account_pnl_partitioned_get**](docs/PnLApi.md#iserver_account_pnl_partitioned_get) | **GET** /iserver/account/pnl/partitioned | PnL for the selected account
*PortfolioApi* | [**portfolio_account_id_allocation_get**](docs/PortfolioApi.md#portfolio_account_id_allocation_get) | **GET** /portfolio/{accountId}/allocation | Account Allocation
*PortfolioApi* | [**portfolio_account_id_ledger_get**](docs/PortfolioApi.md#portfolio_account_id_ledger_get) | **GET** /portfolio/{accountId}/ledger | Account Ledger
*PortfolioApi* | [**portfolio_account_id_meta_get**](docs/PortfolioApi.md#portfolio_account_id_meta_get) | **GET** /portfolio/{accountId}/meta | Account Information
*PortfolioApi* | [**portfolio_account_id_position_conid_get**](docs/PortfolioApi.md#portfolio_account_id_position_conid_get) | **GET** /portfolio/{accountId}/position/{conid} | Position by Conid
*PortfolioApi* | [**portfolio_account_id_positions_invalidate_post**](docs/PortfolioApi.md#portfolio_account_id_positions_invalidate_post) | **POST** /portfolio/{accountId}/positions/invalidate | Invalidates the backend cache of the Portfolio
*PortfolioApi* | [**portfolio_account_id_positions_page_id_get**](docs/PortfolioApi.md#portfolio_account_id_positions_page_id_get) | **GET** /portfolio/{accountId}/positions/{pageId} | Portfolio Positions
*PortfolioApi* | [**portfolio_account_id_summary_get**](docs/PortfolioApi.md#portfolio_account_id_summary_get) | **GET** /portfolio/{accountId}/summary | Account Summary
*PortfolioApi* | [**portfolio_accounts_get**](docs/PortfolioApi.md#portfolio_accounts_get) | **GET** /portfolio/accounts | Portfolio Accounts
*PortfolioApi* | [**portfolio_allocation_post**](docs/PortfolioApi.md#portfolio_allocation_post) | **POST** /portfolio/allocation | Account Alloction (All Accounts)
*PortfolioApi* | [**portfolio_positions_conid_get**](docs/PortfolioApi.md#portfolio_positions_conid_get) | **GET** /portfolio/positions/{conid} | Positions by Conid
*PortfolioApi* | [**portfolio_subaccounts_get**](docs/PortfolioApi.md#portfolio_subaccounts_get) | **GET** /portfolio/subaccounts | List of Sub-Accounts
*PortfolioAnalystApi* | [**pa_performance_post**](docs/PortfolioAnalystApi.md#pa_performance_post) | **POST** /pa/performance | Account Performance
*PortfolioAnalystApi* | [**pa_summary_post**](docs/PortfolioAnalystApi.md#pa_summary_post) | **POST** /pa/summary | Account Balance&#39;s Summary
*ScannerApi* | [**iserver_scanner_params_get**](docs/ScannerApi.md#iserver_scanner_params_get) | **GET** /iserver/scanner/params | get lists of available scanners
*ScannerApi* | [**iserver_scanner_run_post**](docs/ScannerApi.md#iserver_scanner_run_post) | **POST** /iserver/scanner/run | run scanner to get a list of contracts
*SessionApi* | [**iserver_auth_status_post**](docs/SessionApi.md#iserver_auth_status_post) | **POST** /iserver/auth/status | Authentication Status
*SessionApi* | [**iserver_reauthenticate_post**](docs/SessionApi.md#iserver_reauthenticate_post) | **POST** /iserver/reauthenticate | Tries to re-authenticate to Brokerage
*SessionApi* | [**logout_post**](docs/SessionApi.md#logout_post) | **POST** /logout | Ends the current session
*SessionApi* | [**sso_validate_get**](docs/SessionApi.md#sso_validate_get) | **GET** /sso/validate | Validate SSO
*SessionApi* | [**tickle_post**](docs/SessionApi.md#tickle_post) | **POST** /tickle | Ping the server to keep the session open
*TradesApi* | [**iserver_account_trades_get**](docs/TradesApi.md#iserver_account_trades_get) | **GET** /iserver/account/trades | List of Trades for the selected account


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountMaster](docs/AccountMaster.md)
 - [Accounts](docs/Accounts.md)
 - [Allocation](docs/Allocation.md)
 - [AllocationInner](docs/AllocationInner.md)
 - [AllocationInnerAssetClass](docs/AllocationInnerAssetClass.md)
 - [AllocationInnerAssetClassLong](docs/AllocationInnerAssetClassLong.md)
 - [AllocationInnerAssetClassShort](docs/AllocationInnerAssetClassShort.md)
 - [AllocationInnerGroup](docs/AllocationInnerGroup.md)
 - [AllocationInnerGroupLong](docs/AllocationInnerGroupLong.md)
 - [AllocationInnerGroupShort](docs/AllocationInnerGroupShort.md)
 - [AllocationInnerSector](docs/AllocationInnerSector.md)
 - [AllocationInnerSectorLong](docs/AllocationInnerSectorLong.md)
 - [AllocationInnerSectorShort](docs/AllocationInnerSectorShort.md)
 - [AuthStatus](docs/AuthStatus.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [Body5](docs/Body5.md)
 - [Body6](docs/Body6.md)
 - [Body7](docs/Body7.md)
 - [CalendarRequest](docs/CalendarRequest.md)
 - [CalendarRequestDate](docs/CalendarRequestDate.md)
 - [CalendarRequestFilters](docs/CalendarRequestFilters.md)
 - [Contract](docs/Contract.md)
 - [ContractRules](docs/ContractRules.md)
 - [Events](docs/Events.md)
 - [EventsInner](docs/EventsInner.md)
 - [Futures](docs/Futures.md)
 - [FuturesInner](docs/FuturesInner.md)
 - [HistoryData](docs/HistoryData.md)
 - [HistorydataData](docs/HistorydataData.md)
 - [IbcustentityinfoAddress](docs/IbcustentityinfoAddress.md)
 - [IbcustentityinfoEntities](docs/IbcustentityinfoEntities.md)
 - [IbcustentityinfoName](docs/IbcustentityinfoName.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20022E](docs/InlineResponse20022E.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2005Amount](docs/InlineResponse2005Amount.md)
 - [InlineResponse2005Equity](docs/InlineResponse2005Equity.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse2009FilterList](docs/InlineResponse2009FilterList.md)
 - [InlineResponse2009InstrumentList](docs/InlineResponse2009InstrumentList.md)
 - [InlineResponse2009LocationTree](docs/InlineResponse2009LocationTree.md)
 - [InlineResponse2009Locations](docs/InlineResponse2009Locations.md)
 - [InlineResponse2009ScanTypeList](docs/InlineResponse2009ScanTypeList.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse4001](docs/InlineResponse4001.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [Ledger](docs/Ledger.md)
 - [ModifyOrder](docs/ModifyOrder.md)
 - [Notifications](docs/Notifications.md)
 - [NotificationsInner](docs/NotificationsInner.md)
 - [Order](docs/Order.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [Performance](docs/Performance.md)
 - [PerformanceCps](docs/PerformanceCps.md)
 - [PerformanceCpsData](docs/PerformanceCpsData.md)
 - [PerformanceNav](docs/PerformanceNav.md)
 - [PerformanceTpps](docs/PerformanceTpps.md)
 - [Position](docs/Position.md)
 - [PositionInner](docs/PositionInner.md)
 - [ScannerParams](docs/ScannerParams.md)
 - [ScannerparamsFilter](docs/ScannerparamsFilter.md)
 - [Secdef](docs/Secdef.md)
 - [SecdefInner](docs/SecdefInner.md)
 - [SetAccount](docs/SetAccount.md)
 - [Summary](docs/Summary.md)
 - [SummaryAccountSummaries](docs/SummaryAccountSummaries.md)
 - [SummaryBalanceByDate](docs/SummaryBalanceByDate.md)
 - [SummaryBalanceByDateSeries](docs/SummaryBalanceByDateSeries.md)
 - [SummaryExcludedAccounts](docs/SummaryExcludedAccounts.md)
 - [SummaryTotal](docs/SummaryTotal.md)
 - [Symbol](docs/Symbol.md)
 - [Trade](docs/Trade.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



