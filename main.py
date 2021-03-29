# import os
from amazon_scrapper.amazon_scrapper import Amazon
import time


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


import asyncio
from extensions.log import *
# from extensions.stoppable_thread import StoppableThread
# import threading

# import selenium.webdriver.support.expected_conditions as expc

from dotenv import load_dotenv
from os.path import join, dirname
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

itens = [ 
# "https://www.amazon.com/dp/B08L8KC1J7", // Buy now disponivel mas não da pra comprar
"https://www.amazon.com/dp/B08LW46GH2",
"https://www.amazon.com/dp/B08LF1CWT2",
"https://www.amazon.com/Gigabyte-Graphics-WINDFORCE-Protection-DisplayPort/dp/B08WJJNT2R"
]

def main():
    asyncio.run(bot_say('Fala meu irmãooouoou, bora lanchar placa :fork_and_knife:'))
    
    amazon = Amazon()
    threads = amazon.start(itens)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for t in threads:
            t.stop()
        asyncio.run(bot_say('Tchau :call_me:'))

if __name__ == '__main__':
    main()
