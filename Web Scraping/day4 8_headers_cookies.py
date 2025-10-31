# day4_headers_cookies.py
import requests

url = "https://www.baidu.com/"
#在爬虫中，如果不加 Headers，很多网站会返回 403，因为默认的 requests User-Agent 很容易被识别为非浏览器访问。
# 自定义 Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

# 打印响应头
print("响应头:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# 打印 Cookies
print("\nCookies:")
for cookie in response.cookies:
    print(cookie.name, "=", cookie.value)


url = "https://www.zhihu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
print("状态码:", response.status_code)
print(response.text[:500])  # 打印前500字符预览
