import os

import requests
import ujson
import yaml
from utils.RequestsUtil import Request
from config.conf import ConfigYaml

conf_reader = ConfigYaml()
conf_ppv3 = conf_reader.get_conf_value('ppv3')
conf_tianqi = conf_reader.get_conf_value('tianqi')


# 字段值请求
def get_weather():
    url = conf_tianqi['tianqi_url'] \
          + f'?unescape=1&version=v61&appid={conf_tianqi["appid"]}&appsecret={conf_tianqi["appsecret"]}'
    req = Request()
    return req.get(url)


def post_login():
    client_id = conf_ppv3['client_id']
    client_secret = conf_ppv3['client_secret']
    grant_type = conf_ppv3['grant_type']
    username = conf_ppv3['username']
    password = conf_ppv3['password']
    url = conf_ppv3['ppv3_url'] + f'/auth/oauth/token?client_id={client_id}' \
                                  f'&client_secret={client_secret}&grant_type={grant_type}' \
                                  f'&username={username}&password={password}'
    req = Request()
    return req.post(url)


# body请求
def get_activity_lists(token):
    url = conf_ppv3['ppv3_url'] + '/activity/api/promotion/v1/manager/page'
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
    print(get_weather())
    # print(post_login())

