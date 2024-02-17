# qhxc_api

通过该模块可以轻松使用我公司openAPI相关功能。包括交易下单、撤单、查询等功能，目录会根据已实现功能实时更新

## 目录

- [概述](#概述)
- [功能](#功能)
- [安装](#安装)
- [使用](#使用)
- [示例](#示例)

## 概述

通过该模块可以轻松使用我公司openAPI相关功能。包括交易下单、撤单、查询等功能，目录会根据已实现功能实时更新

## 功能


- 创建新订单：实现下单功能
- 根据系统订单号撤销单个订单：撤销指定的未完成订单
- 根据用户自定义订单号撤销单个订单：可撤销单个订单，若自定义订单对应多个系统订单，撤销最新一个订单，撤销申请成功，返回对应的系统订单号
- 根据商品取消所有订单：会查询用户账户下对应商品ID的所有未成交订单，并对这些订单异步进行取消操作
- 根据系统订单号查询单个订单：获取指定订单信息。
- 根据用户自定义订单号查询单个订单：当该自定义订单对应多个系统订单时，只返回最新系统订单。
- 获取交易明细：根据不同的查询条件可获得符合条件的交易明细
- 获取当前的未完结订单：获取没有成交的订单










## 安装

1. 安装依赖模块
2. 安装本功能模块

### 依赖项

列出项目所需的依赖项和版本号。可以使用列表的形式展示。

- requests：2.28.1

### 安装步骤
```
pip install qhxc_api
```
## 使用

使用时导入模块：
```python
from qhxc_api import openapi
```
### 示例

提供一些使用项目的示例代码，以及解释示例的功能和效果。

```python
from qhxc_api import openapi

# 下单示例代码

api = openapi.OpenAPI(host="https://api.xxx.com",
              API_Key="your api key",
              secret="your secret")
res = api.create_order('sell', price='10', size='1', ordertype='limit', funds='', stp='dc', product="ETH_BTC",
                            client_oid="88998889949494")

#根据订单号撤销单个订单示例代码
res = api.cancel_order("your order id")

#根据交易对撤销该交易对下所有订单
api.cancel_orders_product("BTC_USDT")

```
