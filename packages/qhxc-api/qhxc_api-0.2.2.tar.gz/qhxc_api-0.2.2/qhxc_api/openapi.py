from urllib.parse import urljoin
import requests
import time
import hmac
import json
import base64
import hashlib


class OpenAPI(object):
    def __init__(self, host=None, API_Key=None, secret=None):
        self.host = host
        self.API_Key = API_Key
        self.secret = secret
        self.headers = {"Content-Type": "application/json",
                        "Connection": "keep-alive",
                        "Accept-Language": "zh-CN"
                        }

    def generate(self, timestamp, methodtype, repath, send_body, secret):
        methodtype = methodtype.upper()
        if not send_body:
            rehash = timestamp + methodtype + repath
        else:
            body = json.dumps(dict(sorted(send_body.items(), key=lambda v: v[0])), separators=(',', ':'))
            new_body = ''
            for i in body:
                if i == ":" or i == ",":
                    new_body = new_body + i + " "
                else:
                    new_body = new_body + i
            rehash = timestamp + methodtype + repath + new_body
        payload = rehash.encode(encoding='UTF8')
        secret_key = secret.encode(encoding='UTF8')
        digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
        signature = base64.b64encode(digest)
        self.signature = signature.decode('utf-8')
        return self.signature

    # size为市价和限价的数量，funds是市价买时的金额
    def create_order(self, side='', price='', size='', ordertype='', funds='', stp="cn", product=None, client_oid=0):
        if side not in ('buy', 'sell'):
            response = {"code": 400, "msg": "请重新输入side参数。"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        if ordertype not in ('limit', 'market'):
            response = {"code": 400, "msg": "请重新输入order type参数。"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        if stp not in ("dc", "co", "cn", "cb"):
            response = {"code": 400, "msg": "请重新输入自成交策略参数。"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        if ordertype == "limit":
            if not price:
                response = {"code": 400, "msg": "请输入价格参数。"}
                json_data = json.dumps(response, ensure_ascii=False)
                return json_data
            if not size:
                response = {"code": 400, "msg": "请输入数量参数"}
                json_data = json.dumps(response, ensure_ascii=False)
                return json_data
        if ordertype == "market" and side == "buy":
            if not funds:
                response = {"code": 400, "msg": "请输入市价买单金额参数"}
                json_data = json.dumps(response, ensure_ascii=False)
                return json_data
        if not product:
            response = {"code": 400, "msg": "请输入交易对参数"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        sign_path = "/v1/orders"
        uri = '/hk/v1/orders'
        url = urljoin(self.host, uri)
        methodtype = "POST"
        timestamp = str(int(round(time.time() * 1000)))
        body = {
            "client_oid": client_oid,
            "price": price,
            "product": product,
            "side": side,
            "size": size,
            "type": ordertype,
            "funds": funds,
            "stp": stp
        }
        dic_body = dict(sorted(body.items(), key=lambda v: v[0]))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, dic_body, secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.post(url=url, json=dic_body, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 根据订单号撤单
    def cancel_order(self, order_id):
        if not order_id:
            response = {"code": 400, "msg": "请输入订单号"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        deletepath = '/v1/orders/%s' % order_id
        uri = '/hk/v1/orders/%s' % order_id
        url = urljoin(self.host, uri)
        methodtype = "DELETE"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, deletepath, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.delete(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 根据用户自定义订单号撤单
    def cancel_order_client_oid(self, client_oid):
        if not client_oid:
            response = {"code": 400, "msg": "请输入订单号"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        deletepath = '/v1/orders/single/%s' % client_oid
        uri = '/hk/v1/orders/single/%s' % client_oid
        url = urljoin(self.host, uri)
        methodtype = "DELETE"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, deletepath, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.delete(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 根据交易对取消所有该交易对订单
    def cancel_orders_product(self, product):
        if not product:
            response = {"code": 400, "msg": "请输入订单号"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        if '_' not in product:
            response = {"code": 400, "msg": "交易对格式错误，示例：'BTC_USD'"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        deletepath = '/v1/orders?product=%s' % product
        uri = '/hk/v1/orders?product=%s' % product
        url = urljoin(self.host, uri)
        methodtype = "DELETE"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, deletepath, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.delete(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 根据系统订单号查询单个订单
    def get_order(self, order_id):
        if not order_id:
            response = {"code": 400, "msg": "请输入订单号"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        sign_path = '/v1/orders/%s' % order_id
        uri = '/hk/v1/orders/%s' % order_id
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 根据用户自定义订单号查询单个订单
    def get_order_client_oid(self, client_oid):
        if not client_oid:
            response = {"code": 400, "msg": "请输入订单号"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        sign_path = '/v1/orders/single/%s' % client_oid
        uri = '/hk/v1/orders/single/%s' % client_oid
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取交易明细
    def get_fills(self, order_id=None, product=None):
        if order_id:
            sign_path = '/v1/fills?order_id=%s' % order_id
            uri = '/hk/v1/fills?order_id=%s' % order_id
        elif product:
            sign_path = '/v1/fills?order_id=%s' % product
            uri = '/hk/v1/fills?order_id=%s' % product
        else:
            response = {"code": 400, "msg": "order_id或者product_id有一个不能为空"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取当前的未完结订单
    def get_orders(self,order_id=None, product=None):
        if order_id:
            sign_path = '/v1/orders?order_id=%s' % order_id
            uri = '/hk/v1/orders?order_id=%s' % order_id
        elif product:
            sign_path = '/v1/orders?order_id=%s' % product
            uri = '/hk/v1/orders?order_id=%s' % product
        else:
            response = {"code": 400, "msg": "order_id或者product_id有一个不能为空"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取所有资产余额信息
    def get_accounts(self):
        sign_path = '/v1/accounts'
        uri = '/hk/v1/accounts'
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取某个资产余额信息
    def get_accounts_currency(self, currency):
        sign_path = '/v1/accounts/%s' % currency
        uri = '/hk/v1/accounts/%s' % currency
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 资金账户划转到交易账户
    def deposits_account(self, amount, currency):
        sign_path = "/v1/deposits/account"
        uri = '/hk/v1/deposits/account'
        url = urljoin(self.host, uri)
        methodtype = "POST"
        timestamp = str(int(round(time.time() * 1000)))
        body = {
            "amount": amount,
            "currency": currency
        }
        dic_body = dict(sorted(body.items(), key=lambda v: v[0]))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, dic_body, secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.post(url=url, json=dic_body, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 交易账户划转到资金账户
    def withdrawals_account(self, amount, currency):
        sign_path = "/v1/withdrawals/account"
        uri = '/hk/v1/withdrawals/account'
        url = urljoin(self.host, uri)
        methodtype = "POST"
        timestamp = str(int(round(time.time() * 1000)))
        body = {
            "amount": amount,
            "currency": currency
        }
        dic_body = dict(sorted(body.items(), key=lambda v: v[0]))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, dic_body, secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.post(url=url, json=dic_body, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取所有已知的交易产品
    def get_products(self):
        sign_path = '/v1/products'
        uri = '/hk/v1/products'
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取单个产品详情
    def get_product(self, product):
        sign_path = '/v1/products/%s' % product
        uri = '/hk/v1/products/%s' % product
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取K线数据
    def get_kline(self, product, interval, begin, to, size):
        sign_path = '/public/v2/products/%s/candles?interval=%s&from=%s&to=%s&size=%s' % (product, interval, begin, to, size)
        uri = '/hk/public/v2/products/%s/candles?interval=%s&from=%s&to=%s&size=%s' % (product, interval, begin, to, size)
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取订单book数据
    def get_book(self, product, interval):
        if int(interval) > 11:
            response = {"code": 400, "msg": "interval有效取值范围 0-11"}
            json_data = json.dumps(response, ensure_ascii=False)
            return json_data
        sign_path = '/public/v2/products/%s/orderbook?interval=%s' % (product, interval)
        uri = '/hk/public/v2/products/%s/orderbook?interval=%s' % (product, interval)
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 全部币对24小时行情数据
    def get_tickers(self):
        sign_path = '/public/v2/products/overview/tickers'
        uri = '/hk/public/v2/products/overview/tickers'
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取单币对24小时行情数据
    def get_ticker_product(self, product):
        sign_path = '/public/v2/products/%s/ticker' % product
        uri = '/hk/public/v2/products/%s/ticker' % product
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 单币对实时成交数据
    def get_trades_product(self, product, size=500):
        sign_path = '/public/v2/products/%s/trades?size=%s' % (product, size)
        uri = '/hk/public/v2/products/%s/trades?size=%s' % (product, size)
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取所有已知货币
    def get_currencies(self):
        sign_path = '/v1/currencies'
        uri = '/hk/v1/currencies'
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

    # 获取单个币种信息
    def get_currency(self, currency):
        sign_path = '/v1/currencies/%s' % currency
        uri = '/hk/v1/currencies/%s' % currency
        url = urljoin(self.host, uri)
        methodtype = "GET"
        timestamp = str(int(round(time.time() * 1000)))
        secret = self.secret
        sign = self.generate(timestamp, methodtype, sign_path, "", secret)
        self.headers["ACCESS-KEY"] = self.API_Key
        self.headers["ACCESS-SIGN"] = sign
        self.headers["ACCESS-TIMESTAMP"] = timestamp
        try:
            res = requests.get(url=url, headers=self.headers).json()
            return res
        except Exception as e:
            return e

