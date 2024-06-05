import requests

# a = requests.request("GET", "https://www.baidu.com")
a = requests.get("https://www.baidu.com")
print(type(a))
