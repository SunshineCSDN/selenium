from selenium import webdriver
import time

# 生成浏览器示例。根据环境变量找到chromedriver.exe进而驱动chrome.exe
browser = webdriver.Chrome()
browser.get('http://www.douban.com')
time.sleep(6)
browser.quit()  # 关闭退出
