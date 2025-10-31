# day5_bs4_title.py
import requests
from bs4 import BeautifulSoup
#BeautifulSoup 可以把 HTML 文本解析成 树状结构，方便我们快速定位、提取内容。
url = "https://www.baidu.com/"
response = requests.get(url)

# 解析 HTML
soup = BeautifulSoup(response.content, "html.parser")
# 获取 <title> 内容
title = soup.title.string
print("网页标题:", title)
