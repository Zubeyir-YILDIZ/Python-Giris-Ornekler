import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time


class Giriş:
    def __init__(self,kullanıcıAdı,şifre):
        self.tarayıcı=webdriver.Chrome()
        self.kullanıcıAdı=kullanıcıAdı
        self.şifre=şifre
        time.sleep(2)

    def giriş(self):
        self.tarayıcı.get('https://github.com/login')
        email=self.tarayıcı.find_element(By.XPATH,'//*[@id="login_field"]')
        parola=self.tarayıcı.find_element(By.XPATH,'//*[@id="password"]')
        time.sleep(2)
        email.send_keys(self.kullanıcıAdı)
        parola.send_keys(self.şifre)
        time.sleep(2)
        self.tarayıcı.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[11]').click()
        time.sleep(4)

kullanıcıADI=input('Kullanıcı Adı:')
şifre=input('şifre:')
Giriş=Giriş(kullanıcıADI,şifre)
Giriş.giriş()
