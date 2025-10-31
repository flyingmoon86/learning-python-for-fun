import requests

# 创建会话对象
session = requests.Session()

# 模拟登录
login_data = {"username": "test_user", "password": "123456"}
response = session.post("https://httpbin.org/post", data=login_data)

# 查看返回的登录信息
print("登录响应：", response.json())

# 模拟访问需要身份的页面
r2 = session.get("https://httpbin.org/cookies")
print("当前 Cookies：", r2.json())
