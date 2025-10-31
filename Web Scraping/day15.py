# zhihu_hot_fetch.py
import requests
import time
import random
import csv

URL = "https://api.zhihu.com/topstory/hot-list"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
}

def fetch_json(url, headers=None, timeout=8, retries=3, backoff_factor=1.0):
    """
    GET 请求并返回解析后的 JSON，带基本重试机制。
    """
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=timeout)
            # 打印或记录状态码，便于调试
            # print(f"Attempt {attempt}: status={resp.status_code}")
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code in (429, 503):
                # 被限流或服务器繁忙，等候并重试
                wait = backoff_factor * (2 ** (attempt - 1)) + random.uniform(0, 1)
                print(f"Rate limited or service busy ({resp.status_code}), sleeping {wait:.1f}s and retrying...")
                time.sleep(wait)
            else:
                # 其它状态码，视情况处理（可日志记录）
                print(f"Request failed with status {resp.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            wait = backoff_factor * (2 ** (attempt - 1)) + random.uniform(0, 1)
            print(f"Network error on attempt {attempt}: {e}. Retrying in {wait:.1f}s...")
            time.sleep(wait)
    print("Exceeded retries, giving up.")
    return None

def parse_hot_list(json_data):
    """
    从 API 返回的 JSON 中安全提取热榜项。
    返回 list of dict: [{'title':..., 'hot':..., ...}, ...]
    """
    if not json_data:
        return []

    # 如果不确定结构，打印 keys 供调试:
    # print("Top-level keys:", json_data.keys())

    items = []
    # 常见结构：{ "data": [ {item...}, ... ] }
    raw_list = json_data.get("data") or json_data.get("top_stories") or json_data.get("items")
    if not raw_list:
        print("No 'data' list found in JSON.")
        return items

    for obj in raw_list:
        # 用 get() 防止 KeyError
        title = obj.get("title") or obj.get("label") or obj.get("text") or ""
        hot = obj.get("hot") or obj.get("score") or obj.get("weight") or ""
        # 可能还含有链接/ID等字段
        link = obj.get("target") or obj.get("url") or obj.get("link") or ""
        items.append({"title": title, "hot": hot, "link": link})
    return items

def save_to_csv(items, filename="zhihu_hot.csv"):
    if not items:
        print("No items to save.")
        return
    keys = items[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(items)
    print(f"Saved {len(items)} items to {filename}")

def main():
    json_data = fetch_json(URL, headers=HEADERS, timeout=8, retries=4, backoff_factor=1.5)
    if json_data is None:
        print("Failed to get JSON.")
        return

    items = parse_hot_list(json_data)
    for it in items:
        print(it.get("title"), it.get("hot"), it.get("link"))
    save_to_csv(items)

if __name__ == "__main__":
    main()
