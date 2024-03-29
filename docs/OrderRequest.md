# OrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acct_id** | **str** | acctId is optional. It should be one of the accounts returned by /iserver/accounts. If not passed, the first one in the list is selected.  | [optional] 
**conid** | **int** | conid is the identifier of the security you want to trade, you can find the conid with /iserver/secdef/search.  | [optional] 
**sec_type** | **str** | conid:type for example 265598:STK | [optional] 
**c_oid** | **str** | Customer Order ID. An arbitraty string that can be used to identify the order, e.g \&quot;my-fb-order\&quot;. The value must be unique for a 24h span. Please do not set this value for child orders when placing a bracket order.  | [optional] 
**parent_id** | **str** | When placing bracket orders, the child parentId must be equal to the cOId (customer order id) of the parent.  | [optional] 
**order_type** | **str** | orderType can be one of MKT (Market), LMT (Limit), STP (Stop) or STP_LIMIT (stop limit)  | [optional] 
**listing_exchange** | **str** | listingExchange is optional. By default we use \&quot;SMART\&quot; routing. Possible values are available via this end point: /v1/portal/iserver/contract/{{conid}}/info, see valid_exchange: e.g: SMART,AMEX,NYSE, CBOE,ISE,CHX,ARCA,ISLAND,DRCTEDGE,BEX,BATS,EDGEA,CSFBALGO,JE FFALGO,BYX,IEX,FOXRIVER,TPLUS1,NYSENAT,PSX  | [optional] 
**outside_rth** | **bool** | set to true if the order can be executed outside regular trading hours.  | [optional] 
**price** | **float** | optional if order is MKT, for LMT, this is the limit price. For STP this is the stop price.  | [optional] 
**side** | **str** | SELL or BUY | [optional] 
**ticker** | **str** |  | [optional] 
**tif** | **str** | GTC (Good Till Cancel) or DAY. DAY orders are automatically cancelled at the end of the Day or Trading hours.  | [optional] 
**referrer** | **str** | for example QuickTrade | [optional] 
**quantity** | **float** | usually integer, for some special cases can be float numbers | [optional] 
**use_adaptive** | **bool** | If true, the system will use the Adaptive Algo to submit the order https://www.interactivebrokers.com/en/index.php?f&#x3D;19091  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


