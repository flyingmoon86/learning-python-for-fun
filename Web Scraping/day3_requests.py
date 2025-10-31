# day3_requests.py
import requests

url = "https://www.baidu.com/"

# 发送 GET 请求
response = requests.get(url)

# 打印状态码
print("状态码:", response.status_code)

# 保存网页内容
with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("✅ 百度首页已保存为 baidu.html")
