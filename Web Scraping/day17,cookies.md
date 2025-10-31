# 🧩 Day 17：登录与 Cookies 维持

> 目标：学会模拟网站登录、维持会话（Cookies / Session）、并验证登录（例如打印登录后的用户名）。

---

## 🎯 学习目标
- 理解网站登录流程与 Cookie 的作用  
- 使用 `requests.Session()` 模拟登录并维持会话  
- 保存/恢复 Cookies（可选）以免频繁登录  
- 从登录后页面提取并验证用户信息（例如用户名）

---

## 🧠 登录原理
1. 浏览器向服务端发送登录请求（通常是 `POST`），包含表单字段（如 `username`、`password`）。  
2. 服务器验证凭证，登录成功后通过响应头 `Set-Cookie` 返回一个或多个 Cookie（如 `sessionid`）。  
3. 浏览器保存 Cookie；后续对同一站点的请求会自动带上这些 Cookie，服务器据此识别请求属于该用户。  
4. `requests.Session()` 在 Python 中模拟这种“会话”，会自动保存并在后续请求中发送 Cookie。

---

## 🔎 开发者工具（如何找到真实的登录接口）
1. 打开浏览器开发者工具（F12）→ Network → 选择 `XHR` / `Fetch`。  
2. 在登录页面输入凭证并提交，观察产生的请求（通常为 `POST`）。  
3. 点击该请求，查看：  
   - Request URL（接口地址）  
   - Form Data / Request Payload（表单字段名）  
   - Request Headers（重要：Referer、User-Agent、X-CSRF-Token 等）  
   - Response（是否有 `Set-Cookie`）  

记录这些字段，用 `requests` 模拟相同的请求。

---

## ✅ 示例 1 — 最简单的 Session 登录（通用模板）

> 适用于登录表单直接提交用户名/密码且没有 CSRF 或验证码的情况（测试站或简易站点）。

```python
# simple_login.py
import requests

LOGIN_URL = "https://example.com/login"      # 从浏览器 Network 里拿到
PROFILE_URL = "https://example.com/profile"  # 登录后可访问的页面

session = requests.Session()

login_data = {
    "username": "your_username",
    "password": "your_password"
}

# 可加 headers 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://example.com/login"
}

# 发起登录请求
resp = session.post(LOGIN_URL, data=login_data, headers=headers, timeout=10)
print("登录响应状态码：", resp.status_code)

# 登录后的请求（同一 session 会自动带上 cookies）
profile_resp = session.get(PROFILE_URL, headers=headers, timeout=10)
print("个人主页响应状态码：", profile_resp.status_code)
print(profile_resp.text[:800])  # 打印部分 HTML，检查是否含用户名等信息
