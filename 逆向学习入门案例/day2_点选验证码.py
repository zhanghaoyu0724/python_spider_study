import base64
import time

import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as action
from requests_html import HTMLSession


session = HTMLSession()
class BzSpider:
    def __init__(self):
        service = Service('chromedriver')
        self.driver = webdriver.Chrome(service=service)
        self.url = 'https://www.bilibili.com'
        self.mayun_url = "http://api.jfbym.com/api/YmServer/customApi"

    def parse_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span'))).click()

        #/html/body/div[4]/div/div[4]/div[2]/form/div[1]/input
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH,'/html//div[@class="form__item"]/input[@type="text"]'))).send_keys("15873123953")

        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH,'/html//div[@class="form__item"]/input[@type="password"]'))).send_keys("137874120560.0")
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME,'btn_primary'))).click()

        #b站点选验证码
        self.image_data =WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'geetest_widget')))
        self.image_data.screenshot("点选验证码.png")
        self.code_move_calc_function()
        # geetest_item_wrap
    def code_move_calc_function(self):
        with open("点选验证码.png", "rb") as f:
            img_data=f.read()
        base64_data = base64.b64encode(img_data).decode()

        data = {
            'image': base64_data,
            'token': 'kR___Vzwp2ovOrh6UAB_PZsK4GQQ7Hv0ZxBG6kBeTxg',
            'type': '30009'
        }
        resposne =session.post(self.mayun_url, data=data).json()
        print(resposne)
        data = resposne['data']['data']
        self.parse_click_img_html(data)
    def parse_click_img_html(self,data):
        """
        执行鼠标点选
        :param data:
        :return:
        """
        print(data)
        for code_location in data.split('|'):
            xy=code_location.split(',')
            x = int(xy[0])
            y = int(xy[1])
            print(f'{x},{y}')
            #执行点击
            action(self.driver).move_to_element_with_offset(self.image_data,x,y).click().perform()
            time.sleep(0.5)
        self.driver.find_element(By.CLASS_NAME,'geetest_commit').click()
        pass




        pass

if __name__ == '__main__':
    bz=BzSpider()
    bz.parse_login()
    time.sleep(20000)
