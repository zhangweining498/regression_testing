"""
查询某笔交易详情接口
"""
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp

detail_xls = common.get_xls('userCase.xlsx','Detail')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*detail_xls)
class TransactionDetail(unittest.TestCase):

    def setParameters(self,case_name,method,tx_id,coin_type,code,msg):
        '''
        set params
        :param case_name:
        :param method:
        :param tx_id:
        :param coin_type:
        :param code:
        :param msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.tx_id = str(tx_id)
        self.coin_type = str(coin_type)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testDetail(self):
        '''
        查询某笔交易详情
        :return:
        '''
        self.url = common.get_url_from_xml('detail')

        # set url
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # set params
        params = {'tx_id':self.tx_id,
                 'coin_type':self.coin_type}
        configHttp.set_params(params)

        # test interface
        self.return_json = configHttp.request_get()

        self.checkResult()


    def checkResult(self):
        '''
        check test result
        :return:
        '''
        self.info = json.loads(self.return_json.text)
        self.assertEqual(self.info['code'], self.code)
        self.assertEqual(self.info['msg'], self.msg)




if __name__ == '__main__':
    unittest.main()






















