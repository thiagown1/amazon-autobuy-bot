# import os
import time
import asyncio
from extensions.log import *
from amazon_scrapper.amazon_scrapper import Amazon

from dotenv import load_dotenv
from os.path import join, dirname
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

itens = [ 
"https://www.amazon.com/dp/B08L8KC1J7", 
"https://www.amazon.com/dp/B08LW46GH2",
"https://www.amazon.com/dp/B08LF1CWT2",
"https://www.amazon.com/dp/B08KY266MG"
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
