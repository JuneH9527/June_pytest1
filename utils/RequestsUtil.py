import requests
from utils.LogUtil import my_log


class Request:
    def __init__(self):
        self.default_headers = {'Content-Type': 'application/json'}  # 示例默认头信息，根据实际情况调整
        self.log = my_log('requests')

    def request_api(self, method, url, headers=None, json=None, **kwargs):
        if method.lower() == 'get':
            r = requests.get(url, headers=headers, json=json)
        elif method.lower() == 'post':
            r = requests.post(url, headers=headers, json=json)
        status_code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res['status_code'] = status_code
        res['body'] = body
        self.log.debug("【请求结果body】 " + str(res))

        return res

    def get(self, url, **kwargs):
        self.log.debug("发送get请求: " + url)
        return self.request_api('get', url, **kwargs)

    def post(self, url, **kwargs):
        self.log.debug("发送post请求: " + url)
        return self.request_api('post', url, **kwargs)
