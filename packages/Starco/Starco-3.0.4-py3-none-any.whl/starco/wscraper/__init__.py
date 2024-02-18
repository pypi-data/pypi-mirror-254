from functools import wraps
from selenium import webdriver
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from platform import system
import os
from time import sleep
from starco.utils import path_maker
from starco.pkl import Pkl
import json

class WScraper:
    def __init__(self, name,url, browser='firefox',background=False) -> None:
        self.url = url
        self.browser = browser
        self.background=background
        self.driver = self.init_driver()
        self.pkl = Pkl(path_maker()+f'/{name}').pkl
        self.coockies = None
    
    def dec_chk_login(func):
        @wraps(func)
        def magic(self, *args, **kw):
            try:
                return func(self, *args, **kw)
            except Exception as e:
                print(e)
        return magic

    def driver_path(self):
        path=None
        if system() == 'Linux':
            if self.browser == 'chrome':
                path = f"{path_maker(['drivers'])}/chromedriver"
            elif self.browser == 'firefox':
                path = f"{path_maker(['drivers'])}/geckodriver"
        elif system() == 'Windows':
            if self.browser == 'chrome':
                path = f"{path_maker(['drivers'])}/chromedriver.exe"
            elif self.browser == 'firefox':
                path = f"{path_maker(['drivers'])}/geckodriver.exe"
        else:
            raise Exception('Not work on this os')
        if path==None or not os.path.exists(path):
            raise Exception('driver not found')
        return path

    def init_driver(self):
        path = self.driver_path()
        if self.browser == 'chrome':
            cfg= {'service':Service(path)}
            if self.background:
                options = CHOptions()
                options.add_argument("--headless")
                cfg['options']=options
            return webdriver.Chrome(**cfg)
        
        elif self.browser == 'firefox':
            cfg= {'service':Service(path)}
            if self.background:
                options = FOptions()
                options.add_argument("--headless")
                cfg['options']=options
            return webdriver.Firefox(**cfg)

    def save_cookies(self):
        self.pkl('cookies', self.driver.get_cookies())
    
    def save_local_storage(self):
        self.pkl('local_storage', self.driver.execute_script("return window.localStorage;"))
    

    def load_local_storage(self):
        local_storage = self.pkl('local_storage', empty_return={})
        for k,v in local_storage.items():
            if v:
                self.driver.execute_script(f"window.localStorage.setItem('{k}',{json.dumps(v)});")
        self.load_url()

    def load_cookies(self):
        cookies = self.pkl('cookies', empty_return=[])
        if len(cookies) > 0:
            for cookie in cookies:
                try:
                    self.driver.add_cookie(cookie)
                except Exception as e:
                    print(cookie)
            self.coockies = cookies
            self.load_url()

    def check_page_loaded(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'html')))
        
    def check_element(self, by:By, element):
        try:
            self.driver.find_element(by, element)
            return True
        except:
            pass
        return False
   
    def load_url(self,url=''):
        if url =='':url =self.url
        self.driver.get(url)
        self.check_page_loaded()
       
    def fill_input(self,by:By,targe:str,value:str):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, targe)))
        return elem.send_keys(value)
    
    def click(self,by:By,targe:str):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, targe)))
        return elem.click()
    def get_text(self,by:By,targe:str):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, targe)))
        return elem.text
       
if __name__ == "__main__":
    # https://www.karlancer.com/login
    c= WScraper('karlancer','https://www.karlancer.com','chrome')
    c.load_url()
    c.load_local_storage()
    c.load_url('https://www.karlancer.com/panel/dashboard')
    if not c.check_element(By.CLASS_NAME,'icon-message-o'):
        c.load_url('https://www.karlancer.com/login')
        user,password = 'mojtabatahmasbi76m@gmail.com','1112131415'
        c.fill_input(By.NAME,'identifier',user)
        c.fill_input(By.NAME,'password',password)
        c.click(By.ID,'submitButton')
        sleep(5)
        if c.check_element(By.CLASS_NAME,'icon-message-o'):
            c.save_local_storage()
    o= c.get_text(By.XPATH,'/html/body/app-root/app-header-container/app-header-private/nav/div[2]/div[3]/a[5]')
    print(1,o)
    sleep(50)
    