import json
import time

from selenium.webdriver.common.by import By
import pytesseract,base64
from selenium.webdriver.common.action_chains import  ActionChains
from requests_html import HTMLSession

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
"""
超级鹰 ，网易易盾
"""
session = HTMLSession()
# class TWSSpider(object):
#     def __init__(self):
#         self.login_url ="http://www.jianjiaoshuju.com/home/logout.htm"
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.jjsj_url ='http://apigateway.jianjiaoshuju.com/api/v_1/yzmCustomized.html'
#     def parse_login_url(self):
#         self.driver.get(self.login_url)
#         self.driver.find_element(By.CLASS_NAME,"phoneNo").send_keys("15873123953")
#         self.driver.find_element(By.CLASS_NAME,"pwd").send_keys("13787412056zhy")
#         #第一种
#         # self.driver.save_screenshot("验证码识别.png")
#         # img_div =self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/ul/li[3]/div/span/img")
#         # location =img_div.location
#         # #
#         # size =img_div.size
#         #
#         # print(size)
#         # left = location["x"]
#         # top = location["y"]
#         # right = left+size["width"]
#         # bottom = top+size["height"]
#         #
#         # #打开首页验证码
#         # photo = Image.open('验证码识别.png')
#         # print(left,top,right,bottom)
#         # img_obj = photo.crop( (left,top,right,bottom))
#         # img_obj.save("验证码.png")
#         # code =self.parse_start_url()
#         # self.driver.find_element(By.CLASS_NAME,"yzmCode").send_keys(code)
#         # self.driver.find_element(By.CLASS_NAME,"submit-btn").click()
#
#         # text = pytesseract.image_to_string(Image.open('验证码.png'))
#         # print(text)
#
#         #第二种
#
#         img_div = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/ul/li[3]/div/span/img")
#         img_div.screenshot('验证码.png')
#
#     def parse_start_url(self):
#         """
#         对接第三方
#         :return:
#         """
#         headers ={
#             'AppCode' :    '8DBB3BE1909CE219862D6D8FB00B0114',
#             'AppKey':    'AKID998a034b5183b893bccbe3cd108450f2',
#             'AppSecret':'b3d42ffbcccf926455191c8eb9a5615a'
#         }
#         with open('验证码.png','rb') as f:
#             img_data = f.read()
#         base64_data=base64.b64encode(img_data).decode()
#         data={
#             'v_pic':base64_data,
#             'pri_id': 'ne'
#         }
#         response_json =session.post(self.jjsj_url,headers=headers,data=data).json()
#         print(response_json,type(response_json))
#         return response_json['v_code']
#
#
# if __name__ == '__main__':
#     spider = TWSSpider()
#     spider.parse_login_url()
#     spider.parse_start_url()
#     time.sleep(20)


#滑块验证码
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class DBSpider:
    def __init__(self):
        self.url = 'https://www.douban.com'
        service = Service('chromedriver')
        self.driver = webdriver.Chrome(service=service)
        self.yunma_url ='http://api.jfbym.com/api/YmServer/customApi'

    def parse_login_url(self):


        # 填写chromedriver的目录, 此处使用了相对路径


        self.driver.get(self.url)
        self.driver.maximize_window()
        iframe =WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located((By.TAG_NAME,'iframe')))
        self.driver.switch_to.frame(iframe)

        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]'))).click()

        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.ID, 'username'))).send_keys("15873123953")
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.ID, 'password'))).send_keys('13787412056zhy')
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a'))).click()
        time.sleep(2)

        move = self.parse_yzm_function()


        # self.driver.switch_to.parent_frame()
    def parse_yzm_function(self):
        img_iframe = WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.ID, 'tcaptcha_iframe_dy')))

        # 切换到iframe
        self.driver.switch_to.frame(img_iframe)
        img_data =WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slideBg"]')))
        img_data.screenshot('滑块验证码.png')

        """
        将验证码图片交给第三方计算缺口距离，然后使用selenium鼠标操作滑块
        """
        self.parse_code_function()
    def parse_code_function(self):
        with open('滑块验证码.png', 'rb') as f:
            img_data =f.read()
        data =base64.b64encode(img_data).decode()
        data={
            'image': data,
            'token':'kR___Vzwp2ovOrh6UAB_PZsK4GQQ7Hv0ZxBG6kBeTxg',
            'type':'20110'
        }
        move = session.post(url=self.yunma_url,data=data).json()['data']['data']
        #计算完缺口距离
        self.parse_hk_function(move)
    def parse_hk_function(self,move):
        """
        操作selenium 将滑块补全
        :return:
        """
        #定位滑块所在的标签
        #//*[@id="tcOperation"]/div[6]
        bh_div =self.driver.find_element(By.XPATH,'//*[@id="tcOperation"]/div[6]')
        print(move)
        #执行滑块长按滑块
        ActionChains(self.driver).click_and_hold(bh_div).perform()
        time.sleep(0.2)
        #执行鼠标滑动
        ActionChains(self.driver).move_by_offset(xoffset=int(move),yoffset=0,).perform()

        time.sleep(0.5)
        #松开鼠标
        ActionChains(self.driver).release().perform()
        time.sleep(2)
        pass


if __name__ == '__main__':
    spider = DBSpider()
    spider.parse_login_url()
    time.sleep(20)