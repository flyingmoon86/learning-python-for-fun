# day7_re_extract_urls.py
import requests
import re

url = "https://www.baidu.com/"
response = requests.get(url)
html = response.text
#从 HTML 中提取所有 URL 并保存到文件
# 正则匹配 URL
urls = re.findall(r'href="(http[s]?://.*?)"', html)

# 保存到文件
with open("urls.txt", "w", encoding="utf-8") as f:
    for u in urls:
        f.write(u + "\n")

print(f"✅ 共提取 {len(urls)} 个 URL，已保存到 urls.txt")
