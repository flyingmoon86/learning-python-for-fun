import requests
from bs4 import BeautifulSoup
import csv
import time
import random

headers = {"User-Agent": "Mozilla/5.0"}
base_url = "https://movie.douban.com/top250"
all_movies = []

for page in range(0, 10):
    params = {"start": page * 25, "filter": ""}#10*25=250
    response = requests.get(base_url, headers=headers, params=params)
    soup = BeautifulSoup(response.content, "html.parser")
    for item in soup.find_all("div", class_="item"):
        title = item.find("span", class_="title").text
        rating = item.find("span", class_="rating_num").text
        all_movies.append({"title": title, "rating": rating})
    time.sleep(random.uniform(1, 2))  # 随机间隔防封号

# 保存 CSV
with open("movies.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title" , "rating"])
    writer.writeheader()
    writer.writerows(all_movies)

print("✅ 豆瓣 Top250 数据已保存到 movies.csv")
