# -*- coding: UTF-8 -*-
# auther: kele
# 创建时间：2019/1/9 11:23
 
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://szv.122.gov.cn/')
win = driver.current_window_handle
driver.find_element_by_link_text('交通违法罚缴').click()
time.sleep(1)
wins = driver.window_handles
# print(wins)
# driver.switch_to_window(wins[0])
time.sleep(2)
driver.switch_to_window(wins[-1])
time.sleep(10)
driver.find_element_by_css_selector('#indexIsAgree').click()
time.sleep(2)