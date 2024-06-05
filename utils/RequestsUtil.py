import requests

class Request:
    def __init__(self):
        self.default_headers = {'Content-Type': 'application/json'}  # 示例默认头信息，根据实际情况调整

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
        print(r.headers)
        return res

    def get(self, url, **kwargs):
        return self.request_api('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request_api('post', url, **kwargs)
