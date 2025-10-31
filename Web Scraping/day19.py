import requests
import random
import time

# 一组常见的 User-Agent（伪装成不同浏览器）
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/118.0",
]

# 模拟几个代理（这里只是示例，真实爬取需换成可用代理）
PROXIES = [
    {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"},
    {"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"},
]

# 目标网站
url = "https://httpbin.org/get"   # 这个网站会返回你请求的头和IP信息

# 随机选择 UA 和 代理
headers = {"User-Agent": random.choice(USER_AGENTS)}
proxy = random.choice(PROXIES)

print(f"正在使用 UA: {headers['User-Agent']}")
print(f"正在使用代理: {proxy}")

try:
    response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
    print("状态码:", response.status_code)
    print("响应内容:\n", response.text)
except requests.RequestException as e:
    print("请求失败:", e)

# 随机等待 1~3 秒，模拟“人类”操作
time.sleep(random.uniform(1, 3))
