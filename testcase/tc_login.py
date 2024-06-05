import requests

PREFIX_URL = 'https://ppv3-test.yeastar.com'
TIANQI_URL = 'http://v1.yiketianqi.com/api'


# 1. 字段值请求
def get_login():
    login_url = PREFIX_URL + '/auth/oauth/token?client_id=ppv3&client_secret=Yeastar123&grant_type=password&username=pp-d1@yeastar.com&password=Yeastar123'
    r = requests.get(PREFIX_URL + login_url)


def get_tianqi():
    url = TIANQI_URL + '?version=v61&appid=78117444&appsecret=7PeAXEv3'
    r = requests.get(url)
    return r

# 2.json_body请求
def post_activity_lists():
    url = PREFIX_URL + '/activity/api/promotion/v1/manager/page'
    headers = {}
    body = {
        "name": "test",
        "appliedTo": "test",
        "pageSize": 10
    }

    r = requests.post(url, params=body)
    return r.text


if __name__ == '__main__':
    # print(get_tianqi().content.decode())
    # print(get_tianqi().text)
    print(post_activity_lists())
