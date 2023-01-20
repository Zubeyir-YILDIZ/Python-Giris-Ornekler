import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,userName,password):
        self.userName=userName
        self.password=password
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser=webdriver.Chrome(options=opt)
        
    def SignIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.userName)
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button/div").click() #login button
        time.sleep(5)



username_=input('USERNAME: ')
password_=input('PASSWORD: ')

insta=Instagram(username_,password_)
insta.SignIn()