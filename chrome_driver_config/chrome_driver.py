import pickle
import platform
from extensions.log import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class ChromeDriver():
    
    def loadDriver():
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--lang=en-US')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-certificate-errors')
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_experimental_option('useAutomationExtension', False)

        chrome_cap = DesiredCapabilities().CHROME
        chrome_cap["pageLoadStrategy"] = "eager"
        
        if platform.system() == 'Linux': 
            b = webdriver.Chrome(options=chrome_options)
        else:
            chromedriver_path = './win-chromedriver/chromedriver.exe'
            b = webdriver.Chrome(desired_capabilities=chrome_cap,
                                options=chrome_options,
                                executable_path=chromedriver_path)

        b.set_page_load_timeout(5)

        return b

    def loadCookies(driver):
        try: 
            for cookie in pickle.load(open("./cookies", "rb")):
                driver.add_cookie(cookie)
            # l('Cookie loaded...')
            driver.refresh()
        except Exception:
            l('No cookie stored.')
            raise

    def storeCookies(driver):
        pickle.dump(driver.get_cookies(), open("./cookies", "wb")) 
