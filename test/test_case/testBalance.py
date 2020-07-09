'''
打点钱包查询余额接口
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp

payBalance_xls = common.get_xls('userCase.xlsx','Balance')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*payBalance_xls)
class checkBalance(unittest.TestCase):

    def setParameters(self,case_name,method,code,msg):
        '''
        set params
        :param case_name:
        :param method:
        :param code:
        :param cn_msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.code = int(code)
        self.msg = str(msg)

    def description(self):
        '''

        :return:
        '''
        return self.case_name

    def setUp(self):

        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testBalance(self):
        '''
        查询余额
        :return:
        '''
        self.url = common.get_url_from_xml('balance')

        # set url
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # test interface
        self.return_json = configHttp.request_get()


        self.checkResult()

    def checkResult(self):
        '''
        check test result
        :return:
        '''
        self.info = json.loads(self.return_json.text)
        self.assertEqual(self.info['code'],self.code)
        self.assertEqual(self.info['msg'],self.msg)

if __name__ == '__main__':
    unittest.main(verbosity=2)