'''
打点钱包查询流水
'''

import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp

flow_xls = common.get_xls('userCase.xlsx','Flow')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*flow_xls)
class checkFlow(unittest.TestCase):

    def setParameters(self,case_name,method,coin_type,page,page_size,code,msg):
        '''
        set params
        :param case_name:
        :param method:
        :param coin_type:
        :param page:
        :param page_size:
        :param code:
        :param msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.coin_type = str(coin_type)
        self.page = int(page)
        self.page_size = int(page_size)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testFlow(self):
        self.url = common.get_url_from_xml('flow')

        # set url
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # set params
        params = {'coin_type':self.coin_type,
                  'page':self.page,
                  'page_size':self.page_size}
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
        print(self.info)
        self.assertEqual(self.info['code'], self.code)
        self.assertEqual(self.info['msg'], self.msg)

if __name__ == '__main__':
    unittest.main()