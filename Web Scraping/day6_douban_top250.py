# day6_douban_top250.py
import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 提取电影条目
movies = soup.find_all("div", class_="item")

for movie in movies:
    title = movie.find("span", class_="title").text
    rating = movie.find("span", class_="rating_num").text
    print(f"{title} - {rating}")
