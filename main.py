import datetime
import os
import notify
import json
import logging
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import sys


DKYC = ''
DKTIME = ''


class report:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        #self.driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=chrome_options)
        self.__client = webdriver.Chrome(service=Service(
            '/usr/bin/chromedriver'), options=chrome_options)
        self.__wait = WebDriverWait(self.__client, 10, 0.5)

    # def __getText(self,xpath:str):
    #     return self.__wait.until(EC.visibility_of_element_located((By.XPATH,xpath)))

    def __get_element_by_xpath(self, xpath: str):
        return self.__wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def login(self, username: str, password: str) -> bool:
        self.__username = username       
        self.__flag = False
        try:
            self.__client.get(
                "https://yqfk.zcmu.edu.cn:6006/iForm/2714073AABBBDF56AF8E54")
            ids_button = self.__get_element_by_xpath(
                '/html/body/frame-options/div/div/div[2]/div/div/div[3]/ul/li[3]/a')
            ids_button.click()
            uername_input = self.__get_element_by_xpath(
                '/html/body/div[1]/div[4]/div/form/table/tbody/tr[1]/td/input[1]')
            psw_input = self.__get_element_by_xpath(
                '/html/body/div[1]/div[4]/div/form/table/tbody/tr[2]/td/input[1]')
            login_button = self.__get_element_by_xpath(
                '/html/body/div[1]/div[4]/div/form/table/tbody/tr[4]/td/input')
            uername_input.send_keys(username)
            psw_input.send_keys(password)
            login_button.click()
            time.sleep(1)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def do(self, location: str) -> bool:
        try:
            
            select_js = """
                    function getElementByXpath(path) {
                    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    }
                    ele = getElementByXpath(arguments[0]);
                    ele.readOnly = false;
                    ele.value = arguments[1];
                    """
            self.__client.execute_script(
                select_js, '//*[@id="iform"]/div[1]/div[3]/form/div[10]/div/div/div[2]/div/div/div/div[1]/input', location)
            #change = self.__get_element_by_xpath('/html/body/div/div[2]/button[1]')
            #change.click()
            time.sleep(1)
            Q3 = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[10]/div/div/div[2]/div/div/div/div[1]/input')
            Q16 = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[24]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div')
            Q21 = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[30]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div')
            Q22 = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[31]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div')
            Q23 = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[33]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/i')
            Q24 = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[34]/div/div/div[2]/div/div/div/div[1]/div/div[4]/div/i')
            announce = self.__get_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div[3]/form/div[35]/div/div/div[2]/div/div/div/div[1]/div/div/div')
            submit_button = self.__get_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[4]/div/button[1]')
            # change_submit = self.__get_element_by_xpath(
            #    '/html/body/div/div[2]/div[1]/div[4]/div/button')
            Q3.clear()
            Q3.send_keys(location)
            time.sleep(1)
            Q16.click()
            time.sleep(1)
            Q21.click()
            time.sleep(1)
            Q22.click()
            time.sleep(1)
            Q23.click()
            time.sleep(1)
            Q24.click()
            time.sleep(1)
            announce.click()
            time.sleep(1)
            submit_button.click()
            #change_submit.click()
            time.sleep(1)
            # attention = self.__getText(
            #     '/html/body/div[3]/div[1]/div').text  # /html/body/div[3]/div[2]/div
            # print(attention)
            # if attention == '确认提交吗':
            confirm_button = self.__get_element_by_xpath(
                    '/html/body/div[3]/div[3]/button[2]')  # /html/body/div[3]/div[3]/button[2]
            confirm_button.click()
            self.__flag = True
            return True

        except Exception as e:
            logging(e)
            return False

    def check(self) -> bool:
        url = 'https://yqfk.zcmu.edu.cn:5010/Noauth/api/form/api/DataSource/GetDataSourceByNo?sqlNo=SELECT_XSJKDK${}'
        res = json.loads(requests.get(url.format(self.__username)).text)
        global DKYC
        DKYC = res['data'][0]['DKYC']
        # print(res)
        logging.info('Checking data:{}'.format(res))
        if len(res['data']) == 0:
            return False
        unix_dtime = int(time.mktime(datetime.date.today().timetuple()))
        unix_ctime = int(time.mktime(time.strptime(
            res['data'][0]['CURRENTTIME'], '%Y-%m-%d %H:%M:%S')))
        global DKTIME
        DKTIME = res['data'][0]['CURRENTTIME']
        logging.info('unix_dtime: {}, unix_ctime:{}'.format(
            unix_dtime, unix_ctime))
        return True if unix_dtime <= unix_ctime else False
    def pushplus_bot(self,title: str, content: str,token:str,topic:str) -> None:
    # """
    # 通过 push+ 推送消息。
    # """
        
        print("PUSHPLUS 服务启动")

        url = "http://www.pushplus.plus/send"
        data = {
            "token": token,
            "title": title,
            "content": content,
            "topic": topic,
        }
        body = json.dumps(data).encode(encoding="utf-8")
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=url, data=body, headers=headers).json()

        if response["code"] == 200:
            print("PUSHPLUS 推送成功！")

        else:

            url_old = "http://pushplus.hxtrip.com/send"
            headers["Accept"] = "application/json"
            response = requests.post(url=url_old, data=body, headers=headers).json()

            if response["code"] == 200:
                print("PUSHPLUS(hxtrip) 推送成功！")

            else:
                print("PUSHPLUS 推送失败！")
    def reload(self):
        self.__client.get('https://yqfk.zcmu.edu.cn:6006/iForm/2714073AABBBDF56AF8E54')

    def destruct(self):
        self.__client.quit()

    def status(self) -> bool:
        return self.__flag


def main(dev: bool = False):
    retries = 5
    username = os.environ["USERNAME"]
    password = os.environ["PASSWORD"]
    DD_BOT_TOKEN = os.environ["DD_BOT_TOKEN"]
    DD_BOT_SECRET =os.environ["DD_BOT_SECRET"]
    location = os.environ["LOCATION"]
    TOKEN = os.environ["TOKEN"]
    user_list = username.split(',')
    passwd_list = password.split(',')
    
    # location='浙江省/杭州市/富阳区/富春街道'
    #logging.basicConfig(level=logging.INFO, filename="daily.log", filemode="w",
    #                    format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    
    #print(DKYC)
    for i in range(len(user_list)):
        re = report()
        if i != 0 :
            PUSH_PLUS_TOKEN_list  = TOKEN.split(',')
            token = PUSH_PLUS_TOKEN_list[i]
        if re.login(user_list[i], passwd_list[i]):
            if re.check():
                # if dev:
                #     return '已经打过卡了！'
                if DD_BOT_TOKEN:
                    notify.title='Already'
                    notify.content='已经打过卡了！\n打卡状态:%s\n打卡时间:%s' % (DKYC, DKTIME)
                    notify.main()
                
                    if i !=0:
                        if token:
                            re.pushplus_bot('Already','已经打过卡了！\n打卡状态:%s\n打卡时间:%s' % (DKYC, DKTIME),token,'')
            else:
                # if dev:
                #     return '打卡成功！'
                while re.check() != True & retries >= 0 :
                    if re.do(location):
                        logging.info(
                            'succeed: {}'.format(username))
                        re.check()
                        if DD_BOT_TOKEN:
                            notify.title = 'Successful'
                            notify.content = '打卡成功！\n打卡状态:%s\n打卡时间:%s' %(DKYC, DKTIME)                             
                            notify.main()
                        
                            if i !=0:
                                    if token:
                                        re.pushplus_bot('Already','已经打过卡了！\n打卡状态:%s\n打卡时间:%s' % (DKYC, DKTIME),token,'')
                        break
                    retries -= 1
                    re.reload()
                else:
                    # if dev:
                    #     return '打卡失败！'
                    logging.info('error: {}'.format(username))
                    if DD_BOT_TOKEN:
                        notify.title ='ERROR'
                        notify.content='打卡失败！' 
                        notify.main()
                    
                        if i !=0:
                                if token:
                                    re.pushplus_bot('Already','已经打过卡了！\n打卡状态:%s\n打卡时间:%s' % (DKYC, DKTIME),token,'')                
    re.destruct()    
    
if __name__ == "__main__":
    main()
