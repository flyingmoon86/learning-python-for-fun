
#Selenium 是一个自动化测试框架，可以通过程序控制真实浏览器（如 Edge、Chrome、Firefox）。

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# 配置Edge选项
edge_options = Options()
edge_options.add_argument('--start-maximized')  # 启动时最大化窗口
edge_options.add_argument('--disable-extensions')  # 禁用扩展
edge_options.add_argument('--disable-gpu')  # 减少GPU使用
edge_options.add_argument('--no-sandbox')  # 更快的启动

# 使用Edge浏览器
driver = webdriver.Edge(options=edge_options)

try:
    driver.get("https://www.bilibili.com/")
    #让浏览器访问指定网址。
    #相当于人工在地址栏输入网址回车。
    driver.save_screenshot("bilibili_home.png")
    #对整个浏览器可视区域截图，并保存为本地 PNG 文件。
finally:
    driver.quit()  
    # 不管上面执行是否出错，finally 块总会执行。
    # driver.quit() 会关闭浏览器窗口并结束 WebDriver 进程，防止残留占用系统资源。



'''
在数据采集中，我们通常用两种方式抓网页：

类型	工具	特点
静态网页	requests + BeautifulSoup	网页 HTML 源码一次性返回，抓取速度快
动态网页	Selenium	网页内容需要 JS 渲染、滚动加载、点击加载

 获取 动态加载的数据

很多现代网站如知乎、B站、微博、抖音，使用 AJAX / Vue / React。
它们的网页源代码里没有真正的数据，而是通过 JavaScript 动态加载的。

 举个例子：

你用 requests.get() 打开知乎首页，拿到的 HTML 可能只有骨架。

页面里的内容（标题、评论、图片）是浏览器加载后才渲染的。
 Selenium 可以真的“打开浏览器”，等待 JS 执行完，再抓完整的页面。

from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://www.zhihu.com/hot")
print(driver.page_source)  # 这时候内容完整了
'''