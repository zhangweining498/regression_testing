"""
打点钱包发送红包
"""
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp
from common import   Log

redbag_xls = common.get_xls('userCase.xlsx','redbag')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*redbag_xls)
class RedBag(unittest.TestCase):

    def setParameters(self,case_name,method,amount,coin_type,count,info,need_sign,type,code,cn_msg):
        '''
        set params
        :param case_name:
        :param method:
        :param amount:
        :param coin_type:
        :param count:
        :param info:
        :param need_sign:
        :param type:
        :param code:
        :param en_msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.amount = int(amount)
        self.coin_type = str(coin_type)
        self.count = str(count)
        self.info = str(info)
        self.need_sign = bool(need_sign)
        self.type = str(type)
        self.code = int(code)
        self.cn_msg = str(cn_msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testRedBag(self):
        '''
        发红包
        :return:
        '''
        self.url = common.get_url_from_xml('redBag')

        # set url
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # set data
        data = {'amount':self.amount,
                'coin_type':self.coin_type,
                'count':self.count,
                'info':self.info,
                'need_sign':self.need_sign,
                'type':self.type}
        configHttp.set_data(data)

        # test interface
        self.return_json = configHttp.request_json_post()

    def checkResult(self):
        '''
        check test result
        :return:
        '''
        self.info = json.loads(self.return_json.text)
        self.assertEqual(self.info['code'], self.code)
        self.assertEqual(self.info['cn_msg'], self.cn_msg)





if __name__ == '__main__':
    unittest.main()



