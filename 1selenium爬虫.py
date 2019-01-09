from selenium import webdriver
from lxml.html import fromstring
import time
driver = webdriver.Chrome()
driver.get('http://exercise.kingname.info/exercise_ajax_2.html')
time.sleep(2)
html = driver.page_source
dom1 = fromstring(html)
x = dom1.xpath('/html/body/div/text()')
print(x)
driver.quit()
