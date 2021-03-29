import os
import time
import random
import pickle
import asyncio
from extensions.log import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as expc

from amazoncaptcha import AmazonCaptcha
from chrome_driver_config.chrome_driver import *
from extensions.stoppable_thread import StoppableThread


LOGIN_MAIL = os.environ.get("MAIL_ADDRESS")
LOGIN_PASSWORD = os.environ.get("PASSWORD")
LOGIN_URL = os.environ.get("LOGIN_URL")

class Amazon:

    threads = []
    urls = []
    
    @staticmethod
    def fillUsername(d: webdriver.Chrome):
        d.find_element_by_id('ap_email').send_keys(LOGIN_MAIL)
        d.find_element_by_id('continue').click()
    
    @staticmethod
    def fillPassword(d: webdriver.Chrome):
        d.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
        d.find_element_by_name('rememberMe').click()
        d.find_element_by_id('signInSubmit').click()

    def login(self, d: webdriver.Chrome):
        try:
            d.get('https://www.amazon.com')

            logged = False
            for cookie in d.get_cookies():
                if cookie['name'] == 'sess-at-main':
                    logged = True

            if not logged:
                l('not logged')
                d.get(LOGIN_URL)
                l('Opened')

                try:
                    self.fillUsername(d)
                    self.fillPassword(d)
                except:
                    l('Login failed!!!')
                    pass
            
            l('Logged')
            d.get('https://www.amazon.com')
            l('Storing cookies!')
            pickle.dump(d.get_cookies(), open("./cookies", "wb")) 
            d.quit()
            
        except Exception as inst:
            l('Failed to open browser.')  

    @staticmethod
    def solveCaptcha(d: webdriver.Chrome):
        if 'Amazon.com' == d.title: 
            try:
                time.sleep(random.randint(1,3))
                captcha = AmazonCaptcha.fromdriver(d).solve()
                print(captcha + 'doc: ' + d.page_source)
                d.find_element_by_id('captchacharacters').send_keys(captcha)
                d.find_element_by_tag_name('button').click()
            except:
                l('Unable to pass captcha!!!')

    def unlockBuyNow(self, d: webdriver.Chrome):
        d.get("https://www.amazon.com")
        ChromeDriver.loadCookies(d)
        d.get('https://www.amazon.com/gp/css/homepage.html?ref_=nav_youraccount_btn')
        
        self.solveCaptcha(d)

        d.find_element_by_xpath("//div[@data-card-identifier='GiftCards']").click()

        if 'signin' in d.current_url:
            try:
                self.fillUsername(d)
                self.fillPassword(d)
            except:
                self.fillPassword(d)
                
            
            ChromeDriver.storeCookies(d)

        l('Unlocked buy now')

    def tryToBuy(self, url: str):
        
        firstLoad = True
        d: webdriver.Chrome = ChromeDriver.loadDriver()
        try:
            self.unlockBuyNow(d)
        except Exception as e:
            l(d.title + 'Failed to unlock buy now: ' + e.__str__())
        time.sleep(4)

        count = 0
        lastTimeSaid = -1
        gpuName = 'GPU Not loaded'
        d.get(url)

        while True:
            try:    
                
                ChromeDriver.loadCookies(d)
            
                wait = WebDriverWait(d, 5)
                wait.until(expc.title_contains('RTX'))
                wait.until(expc.presence_of_element_located((By.ID,'productTitle')))
                productTitle = d.find_element_by_id('productTitle')
                
                count += 1
                title = str(productTitle.text)
                
                try:
                    gpuName = title[title.index('RTX'):title.index('RTX') + 8] + ' - ' + title.split(' ')[0]
                except:
                    gpuName = title
                    l('Not GPU... rtx')

                if datetime.now().minute == 30 or datetime.now().minute == 0:
                    if lastTimeSaid != datetime.now().minute:
                        lastTimeSaid = datetime.now().minute
                        asyncio.run(bot_say('Tentando comprar ' + gpuName + ' :see_no_evil: :clock1230: Tentativa: ' + str(count)))

                if firstLoad:
                    l('Primeiro load')
                    firstLoad = False
                    asyncio.run(bot_say('Tentando comprar ' + gpuName + ' :see_no_evil: '))
        
                l('Trying: ' + gpuName + ' Tries: ' + str(count))
                d.find_element_by_id('buy-now-button').click()
                asyncio.run(bot_say('Buy now disponível para ' +  gpuName  + ' :speak_no_evil: '))
            
                if 'signin' in d.current_url:
                    d.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
                    d.find_element_by_id('signInSubmit').click()
                    asyncio.run(bot_say('Solicitou login'))

                d.find_element_by_id('placeYourOrder')
                asyncio.run(bot_say('Comprada!!! ' +  gpuName  + ' :monkey_face: '))

                for t in self.threads:
                    t.stop()

            except Exception as e:
                self.solveCaptcha(d)
                l('No stock! ' + gpuName)
                time.sleep(random.randint(1,14) / 10 + 0.6)

    def start(self, urls):
        for i in range(len(urls)):
            t = StoppableThread(target=self.tryToBuy, args=(urls[i],))
            t.daemon = True
            
            t.name = i
            self.threads.append(t)

        for t in self.threads:
            t.start()

        return self.threads
