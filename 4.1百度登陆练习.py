from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get(url='https://passport.baidu.com/v2/?login')


elemt = brower.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn')
elemt.click()

elemt = brower.find_element_by_id('TANGRAM__PSP_3__userName')
elemt.send_keys('MySunshinedgg')
elemt = brower.find_element_by_id('TANGRAM__PSP_3__password')
elemt.send_keys('ma17796734091')
su = brower.find_element_by_id('TANGRAM__PSP_3__submit')
      # 打印标签名
su.click()       #(常用）鼠标单击
time.sleep(20)
brower.close()