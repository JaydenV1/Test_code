from Common.BaseApi import Request
from Common.handel_path import Test_config_path
from Common.handel_yaml import get_yaml
import copy
import unittest
from Common.custom_log import error_log,info_log


class TestCreateOption(unittest.TestCase):
    biz_date = None
    HOST = get_yaml(Test_config_path)['HOST']
    PATH = '/trade/entry/add/option/trade'
    URL = HOST + PATH
    TOKEN = get_yaml(Test_config_path)['US_TOKEN']
    BODY = [
        {
            "companyId": "-6922148354643243027",
            "balanceType": "07",
            "businessThruDate": "4821-12-27",
            "processInDate": "2022-02-28",
            "processOutDate": "4821-12-27",
            "source": "01",
            "externalRefId": "1010155573997469696",
            "initiatorType": "02",
            "initiatorId": "zhongjian",
            "lastUpdateType": "02",
            "lastUpdateBy": "zhongjian",
            "updateTime": "2022-08-18T22:27:38.000Z",
            "createTime": "2022-08-18T19:57:37.000Z",
            "tradeType": "01",
            "tradeCode": "18",
            "dealType": "13",
            "direction": "01",
            "orderType": '',
            "orderNumber": '',
            "executionTime": "",
            "executionBroker": '',
            "exchangeId": '',
            "member": '',
            "blotterCode": '',
            "primaryAccountNo": "zj002",
            "primaryAccountId": "-1140549394411536358",
            "primaryAccountType": "client_account",
            "primaryAccountSubType": "hedge",
            "primaryPartyId": "2995219152365701724",
            "contraPartyId": "0",
            "contraAccountId": "-3222620769426388608",
            "contraAccountName": '',
            "contraAccountNo": "SFB5407",
            "servicePartyId": "0",
            "serviceAccountId": "-4696178612537833219",
            "serviceAccountName": '',
            "serviceAccountNo": "MBGM",
            "quantity": 1000000,
            "unit": '',
            "price": 127.25,
            "amount": 127250000,
            "priceCurrency": "USD",
            "settlementCurrency": "JPY",
            "orderChannel": "Voice",
            "traderId": '',
            "remark": "fx option exercise",
            "productId": "41357627489798878",
            "product": {
                "referenceId": '',
                "leftParent": "-8842160400517348518",
                "rightParent": '',
                "productId": "41357627489798878",
                "status": 1,
                "description": "USDJPY-O",
                "source": "MANUAL",
                "securityType": "fx_option",
                "assetType": "fxoption",
                "listStatus": '',
                "createTime": "2021-04-15 02:03:54",
                "createBy": "zhongjian",
                "updateTime": "2022-06-30 02:41:05",
                "updateBy": "zhongjian",
                "updateReason": "",
                "exchangeId": '',
                "baseCurrency": "USD",
                "settlementCurrency": "JPY",
                "attributes": {
                    "option_style": "european",
                    "option_type": "vanilla",
                    "trading_ccy_base_rate": "1802",
                    "settlement_ccy_base_rate": "26101"
                },
                "symbols": {
                    "currency_pair": {
                        "value": "USDJPY",
                        "symbolTimelineList": [
                            {
                                "value": "USDJPY",
                                "status": 1,
                                "major": True,
                                "createTime": "2021-04-15 02:03:54",
                                "updateTime": "2022-06-30 02:41:05"
                            }
                        ]
                    }
                },
                "relatedTo": '',
                "symbol": ''
            },
            "parentProductId": '',
            "parentProductDesc": '',
            "productExchangeId": '',
            "productExchangeCode": '',
            "settlementDate": "2022-03-01",
            "productDescription": "USDJPY-O",
            "productSymbol": '',
            "primaryAccountSub": "",
            "contraAccountSub": "",
            "serviceAccountSub": "",
            "productAssetType": "fxoption",
            "productSecurityType": "fx_option",
            "commission": '',
            "fees": '',
            "groupAccountId": '',
            "groupAccountNumber": '',
            "groupAccountName": '',
            "commissionFeeOverride": [],
            "freezeFeeTypes": '',
            "originalTradeEntryId": '',
            "verifiedTime": "2022-08-18T22:27:37.000Z",
            "verifiedBy": "summer2",
            "offsetPosition": '',
            "priceUnit": '',
            "priceDecimalPoint": '',
            "priceDenominator": '',
            "houseAccountId": "-4696178612537833219",
            "houseAccountNo": "MBGM",
            "houseAccountType": "house_trading_account",
            "houseAccountSubType": "house_trading_account",
            "ibAccountNo": '',
            "ibAccountName": '',
            "lpAccountId": "-3222620769426388608",
            "lpAccountNo": "SFB5407",
            "lpAccountType": "broker_account",
            "lpAccountSubType": "fx_clearing_broker_account",
            "pbAccountId": "-3222620769426388608",
            "pbAccountNo": "SFB5407",
            "pbAccountName": "SUMFB5407",
            "pbAccountType": "broker_account",
            "pbAccountSubType": "fx_clearing_broker_account",
            "bookType": "A",
            "executionId": '',
            "orderId": '',
            "dealSource": "01",
            "waiveCommission": "Y",
            "houseBalanceType": "03",
            "lpBalanceType": "03",
            "decimalPoint": 5,
            "postingDate": '',
            "settlementMethod": "1",
            "optionCut": "TOK",
            "fixingSource": '',
            "underlyingSide": "C",
            "underlyingContractAmount": "1000000",
            "underlyingStrikePrice": "127.25",
            "underlyingTermAmount": "127250000.00",
            "optionPremiumRateType": "2",
            "optionPremiumDealtCurrency": "JPY",
            "optionPremiumCurrency": "USD",
            "optionPremiumRate": 2,
            "optionPremiumCPRate": 0.8618,
            "optionPremiumAmount": 2545000.02,
            "optionPremiumCPAmount": -1096641,
            "pipsPoints": "0.01",
            "reversalPipsPoints": "0.00001",
            "optionStyle": '',
            "verifiedTimeStr": "2022-08-19 06:27:37",
            "createTimeStr": "2022-08-19 03:57:37",
            "updateTimeStr": "2022-08-19 06:27:38",
            "postDateStr": "2022-02-28",
            "tradeDateStr": "2023-02-28",
            "tradeTimeStr": "",
            "tradeTime": "2022-08-19T08:36:51.507Z",
            "verifiable": False,
            "deleteable": True,
            "rejectable": False,
            "editable": True,
            "executionTimeStr": '',
            "fixingDateStr": "",
            "expiryDateStr": "2022-02-28",
            "premiumDateStr": "2021-03-01",
            "underlyingFinalSettlementDateStr": "2022-03-01",
            "oDirection": "02",
            "oUnderlyingSide": "P",
            "pbAccount": {
                "id": "-3222620769426388608",
                "accountCode": "-3222620769426388608",
                "symbolType": "account_name",
                "symbolValue": "SUMFB5407",
                "status": 1,
                "accountName": "SUMFB5407",
                "accountNumber": "SFB5407",
                "accountType": "broker_account",
                "accountSubType": "fx_clearing_broker_account",
                "value": "-3222620769426388608"
            },
            "overrideCommissionData": [],
            "postDate": "2022-03-01",
            "tradeDate": "2022-02-28",
            "fixingDate": '',
            "expiryDate": "2023-02-28",
            "premiumDate": "2023-03-01",
            "underlyingFinalSettlementDate": "2023-03-01",
            "primaryAccountName": "xieguanbin"
        }
    ]

    @classmethod
    def setUpClass(cls):
        """获取实时biz date"""
        path = '/eod/all-business-date'
        url = cls.HOST + path
        try:
            res = Request.get_request(url=url, token=cls.TOKEN)
            info_log(res.status_code)
            info_log(res.text)
            cls.biz_date = res.json()['data'][0]['businessDate']
            return cls.biz_date
        except Exception as e:
            error_log(f'python执行时的错误：{e}')
            return e

    def test001_option(self):
        """input_checkout:测试输入已过期的post date参数"""
        resp = Request.post_request(url=self.URL, body=self.BODY)
        self.assertEqual(422, resp.status_code)

    def test_option_002(self):
        """测试body=[]的参数类型"""
        body = []
        resp = Request.post_request(url=self.URL, body=body, token=self.TOKEN)
        print(resp.json())
        self.assertEqual(422, resp.status_code)

    def test_option_003(self):
        """测试body为str的参数类型"""
        body = "str"
        resp = Request.post_request(url=self.URL, body=body, token=self.TOKEN)
        print(resp.json())
        self.assertEqual(500, resp.status_code)

    def test_option_004(self):
        """传入实时的biz-date是否正常运行"""
        body = copy.deepcopy(self.BODY)
        body[0].update(postDate=self.biz_date)
        resp = Request.post_request(url=self.URL, body=body, token=self.TOKEN)
        print(resp.json())
        self.assertEqual(200, resp.status_code)

    def test_option_005(self):
        """不传入token就进行请求"""
        body = copy.deepcopy(self.BODY)
        body[0].update(postDate=self.biz_date)
        resp = Request.post_request(url=self.URL, body=body, token=None)
        self.assertEqual('Not Login', resp.json()['msg'])
        self.assertEqual(401, resp.status_code)

    def test_option_006(self):
        """不传入body时查看接口的响应情况"""
        resp = Request.post_request(url=self.URL, body=None, token=self.TOKEN)
        print(resp.json())
        self.assertEqual("action failed", resp.json()['msg'])
        self.assertEqual(500, resp.status_code)

    def test_option_007(self):
        """传入不合法的account，接口的响应情况"""
        body = copy.deepcopy(self.BODY)
        body[0].update(primaryAccountId="123456654321")
        resp = Request.post_request(url=self.URL, body=body)
        print(resp.json())
        self.assertEqual(500,resp.status_code)

    def test_option_008(self):
        """传入数据库中没有的product，接口的响应情况"""
        body = copy.deepcopy(self.BODY)
        body[0].update(productId="123456654321")
        resp = Request.post_request(url=self.URL, body=body)
        print(resp.json())
        self.assertEqual(404,resp.status_code)
        self.assertIn("ProductVO not found!", resp.json()['description'])


