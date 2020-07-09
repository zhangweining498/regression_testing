import readConfig
from common.Log import MyLog as MyLog
from common.common import get_headers
import requests,json


localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global scheme, host, port, timeout

        scheme = localReadConfig.get_http('scheme')
        host = localReadConfig.get_http('baseurl')
        port = localReadConfig.get_http('port')
        # timeout = localReadConfig.get_http('timeout')
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data= {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_headers(self):
        '''
        set headers
        :return:
        '''
        self.headers = get_headers()

    def set_url(self,url):
        '''
        set url
        :param url:
        :return:
        '''
        self.url = scheme + '://' + host + url

    # def set_headers(self):
    #     '''
    #     set headers
    #     :param header:
    #     :return:
    #     '''
    # def set_params(self, param):
    #     """
    #     set params
    #     :param param:
    #     :return:
    #     """
    #     self.param = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_params(self,params):
        '''
        set params
        :param params:
        :return:
        '''
        self.params = params

    def request_get(self):
        '''
        defind get method
        :return:
        '''
        try:
            response = requests.get(self.url, headers = self.headers, params=self.params)
            res_data = json.loads(response.text)
            self.logger.info(res_data + '\n')
            return response
        except Exception as ex:
            self.logger.error(ex)
            return None



    def request_json_post(self):
        '''
        defind post method,make json
        :return:
        '''
        try:
            response = requests.post(self.url, headers = self.headers, json = self.data)
            res_data = json.loads(response.text)
            self.logger.info(res_data)
            return response
        except Exception as ex:
            self.logger.error(ex)
            return None

if __name__ == '__main__':
    c = ConfigHttp()
    url = '/api/v1/payAddress'
    data  = {'address':'1MjUodGyHSFXcmaBmsMnTLtgyrBtTEHxd4',
                'amount':1000,
                'coin_type':'BSV',
                'info':'',
                'need_sign':True}
    c.set_url(url)
    c.set_data(data)
    res = c.request_json_post()
    print(res.text)
    # print(res.text)

