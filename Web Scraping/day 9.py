import requests
from bs4 import BeautifulSoup
import time
import random
import csv

base_url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0"}
all_movies = []

for page in range(0, 10):
    params = {"start": page * 25, "filter": ""}
    response = requests.get(base_url, headers=headers, params=params)
    
    # 解析 HTML
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", class_="item")
    
    for item in items:
        title = item.find("span", class_="title").text
        rating = item.find("span", class_="rating_num").text
        all_movies.append({"title": title, "rating": rating})
    
    # 随机等待 1~2 秒，防封号
    time.sleep(random.uniform(1, 2))

# 保存到 CSV
with open("movies.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "rating"])
    writer.writeheader()
    writer.writerows(all_movies)

print("✅ 爬取完成，数据已保存到 movies.csv")
