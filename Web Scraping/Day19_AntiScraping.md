# Day 19：反爬策略（随机 User-Agent、代理 IP）

## 🎯 学习目标
- 使用随机 **User-Agent** 来降低被识别为爬虫的概率  
- 使用 **代理 IP** 提高匿名性与绕过简单的 IP 限制  

---

## 一、为什么需要这些策略？
- 许多网站通过检测请求头（如 `User-Agent`）或短时间内大量请求来自同一 IP 来判定非人类流量，从而返回 403、429 或直接封禁 IP。  
- 通过**随机化 User-Agent**、**使用代理池**和**控制访问频率**，可以显著降低被封的风险，但不能保证百分之百安全。

---

## 二、示例代码（基础版：随机 UA + 单代理）

```python
import requests
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "https://127.0.0.1:8080"
}

headers = {"User-Agent": random.choice(user_agents)}
response = requests.get("https://www.example.com", headers=headers, proxies=proxies, timeout=8)
print(response.status_code)
```

---

## 三、进阶用法（代理池 + 重试 + 随机延时）

建议结合代理池、重试机制和随机等待来提高稳定性。

```python
import requests
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    # ... 更多 UA
]

PROXY_POOL = [
    "http://1.2.3.4:8000",
    "http://5.6.7.8:8000",
    # ... 更多代理
]

def get_proxy_dict(proxy_url):
    return {"http": proxy_url, "https": proxy_url}

def fetch(url, retries=3):
    for attempt in range(retries):
        ua = random.choice(USER_AGENTS)
        proxy = random.choice(PROXY_POOL)
        headers = {"User-Agent": ua}
        try:
            r = requests.get(url, headers=headers, proxies=get_proxy_dict(proxy), timeout=8)
            if r.status_code == 200:
                return r
            else:
                print("状态码:", r.status_code)
        except requests.RequestException as e:
            print("请求异常:", e)
        wait = random.uniform(1, 3)
        time.sleep(wait)
    return None
```

---

## 四、代理类型与获取途径
- **透明代理 / 匿名代理 / 高匿代理**：高匿代理更难被目标站点识别为代理。  
- **免费代理**：不可靠、速度慢且常失效，适合学习和测试。  
- **付费代理服务**：更稳定，支持大量并发与地理位置选择（推荐生产环境使用）。  
- **购买或搭建私有代理池**：长期稳定性最优，但需要运维成本。

---

## 五、实践建议与注意事项
- **不要滥用代理**：频繁请求仍会被目标方发现并封禁代理IP。  
- **遵守网站使用条款**：爬取前查看 `robots.txt`、服务条款及法律合规要求。  
- **结合频率控制**：使用 `time.sleep()` 或令牌桶算法控制请求速率。  
- **日志与监控**：记录请求成功率、代理失效率，及时替换失效代理。  
- **安全**：不要把敏感凭证放在公开仓库；代理会看到你发出的数据（避开明文敏感信息）。

---

## 六、常见问题（FAQ）
- **Q：随机 UA 就足够了吗？**  
  A：不是，UA 只是识别因素之一。还要配合 IP 轮换、Referer、Cookies、模拟行为等。

- **Q：免费代理行不行？**  
  A：短期试验可以，但长期或批量爬取不推荐，稳定性和安全性都无法保证。

---

## 参考
- `requests` 文档：https://requests.readthedocs.io/  
- 代理服务/池工具：例如 `proxybroker`、`scrapy-rotating-proxies`（在 Scrapy 中常用）  
