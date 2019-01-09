from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://exercise.kingname.info/exercise_login.html')
elem1 = browser.find_element_by_name("username")
elem1.send_keys("kingname")

elem2 = browser.find_element_by_name("password")
elem2.send_keys("genius")

elem3 = browser.find_element_by_tag_name('button')
elem3.click()

time.sleep(20)
browser.close()