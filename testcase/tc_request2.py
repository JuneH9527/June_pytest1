import requests
import ujson
from utils.RequestsUtil import Request
import yaml

PPV3_URL = 'https://ppv3-test.yeastar.com'
TIANQI_URL = 'http://v1.yiketianqi.com/api'


# 字段值请求
def get_weather():
    appid = '78117444'
    appsecret = '7PeAXEv3'
    url = TIANQI_URL + f'?unescape=1&version=v61&appid={appid}&appsecret={appsecret}'
    req = Request()
    return req.get(url)


def post_login():
    with open('../data.yml', 'r') as f:
        data = yaml.safe_load(f)
    client_id = data['ppv3']['client_id']
    client_secret = data['ppv3']['client_secret']
    grant_type = data['ppv3']['grant_type']
    username = data['ppv3']['username']
    password = data['ppv3']['password']
    url = PPV3_URL + f'/auth/oauth/token?client_id={data["ppv3"]["client_id"]}' \
                     f'&client_secret={client_secret}&grant_type={grant_type}' \
                     f'&username={username}&password={password}'
    req = Request()
    return req.post(url)


# body请求
def get_activity_lists(token):
    url = PPV3_URL + '/activity/api/promotion/v1/manager/page'
    body = {
        "name": "test",
        "appliedTo": "test",
        "pageSize": 10
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    req = Request()
    req.get()


if __name__ == '__main__':
    # print(get_weather())
    print(post_login())
