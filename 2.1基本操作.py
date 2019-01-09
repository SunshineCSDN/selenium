from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

# 打开，退出浏览器，请求网页
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# time.sleep(5)
# driver.close()

# 打开测试页面
# 无头模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)

# 普通模式
browser = webdriver.Chrome()
browser.get('file:///D:/PycharmProjects1/tutorial/L47selenium/2index.html')
time.sleep(2)

# 1> (常用)根据id或name值查找标签，打印标签属性，文本
# 实质上也是先lxml转换成文档树，类似xpath,js,bs
elemt = browser.find_element_by_id('element_id')
elemt2 = browser.find_element_by_name('element_id')
print(elemt)

# 2> 取标签中值，属性
print(browser.find_element_by_tag_name('label').text)  # 标签内容
print(elemt.get_attribute('id'))  # 取属性

# 3》 给标签中输入文本

elemt.send_keys('咋设置')
time.sleep(5)

#4（了解）>根据标签内容选择标签
elemt = browser.find_element_by_link_text('find_element_by_link_text')
print(elemt.tag_name)  # 打印标签名
elemt.click()  # (常用) 鼠标单击
time.sleep(1)

# 5（了解）>根据css选择器选择元素

elemt = browser.find_element_by_css_selector(".highlight")
elemt.send_keys("啦啦啦")
time.sleep(2)

# 6 (常用)根据xpath选择元素
elemt = browser.find_element_by_xpath('//*[@id="xpathname"]')
elemt.send_keys('根据xpath')
time.sleep(2)

# 7.切换标签页 获取页面源代码
browser.switch_to.window(browser.window_handles[0])
print(browser.page_source)
time.sleep(2)

# 8>跳转到弹窗，接受
# 操作弹出框

# elem = browser.find_element_by_tag_name("button")
# elem.click()
# time.sleep(2)
# browser.switch_to.alert.accept()

# 9> 跳转和回退
# elemt = browser.find_element_by_partial_link_text('forward_back')
# elemt.click()
# time.sleep(1)
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)

# 10> cookie
# print(browser.get_cookies())
# browser.add_cookie({'name':'test','domain':'ww.baidu.com'})
# print(browser.get_cookies())

# 11>键盘特殊按键
elemt.send_keys(Keys.RETURN)  # Keys.ENTER




browser.quit()

"""
(了解)无偷浏览器模式
无头模式：浏览器后台运行，并不展示窗口页面，有利于节省资源提升速度。phantomjs,一个过去流行的无头的浏览器工具。因为ie,chrome等现代浏览器

"""