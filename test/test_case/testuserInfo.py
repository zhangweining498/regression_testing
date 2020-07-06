'''
打点钱包获取用户信息
'''
import readConfig
import json
import unittest,paramunittest
from common import common,Log
from common import configHttp

userInfo_xls = common.get_xls('userCase.xlsx','userInfo')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = ()

@paramunittest.parametrized(*userInfo_xls)
class UserInfo(unittest.TestCase):

    def setParameters(self,case_name,method,code,cn_msg):
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
        self.cn_msg = str(cn_msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testuserInfo(self):
        self.url = common.get_url_from_xml('userInfo')

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
        self.assertEqual(self.info['cn_msg'],self.cn_msg)

if __name__ == '__main__':
    unittest.main()