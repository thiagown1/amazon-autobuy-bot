import time
import random
import requests

from bs4 import BeautifulSoup

class ProxyManager:

    proxy_list = []

    def load_list(self, code: str = "US"):
        res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(res.text,"html.parser")
        
        self.proxy_list = []

        for items in soup.select("#proxylisttable tbody tr"):
        
            proxies = ':'.join([item.text for item in items.select("td")[:2]])
            country = items.select("td")[2].text
        
            if country == code:
                self.proxy_list.append(proxies)

    def getRandomProxy(self):

        if len(self.proxy_list) == 0: self.load_list()

        new_proxy = self.proxy_list[random.randint(0, len(self.proxy_list) - 1)]

        return new_proxy

    def handle_refresh(self):
        while True:
            time.sleep(3600)
            self.load_list()
    