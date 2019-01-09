# 练习
"""
目标：打开浏览器，打开百度，搜素框内填充关键字，单击百度一下按钮，网页向下翻，点击第二页，打印结果列表标题。


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://baidu.com')
assert "百度" in browser.title
elem = browser.find_element_by_id("kw")
# print(elem)
elem.send_keys("python")
elem.send_keys(Keys.RETURN)


time.sleep(20)
browser.close()

# 参考文章https://www.cnblogs.com/orangeseason/p/4627765.html