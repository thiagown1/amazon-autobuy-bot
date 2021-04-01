# Amazon Automation

Python script (This is my first python script... Maybe errors, recommended use just for reference)

 - Set urls for products (Currently only looking for 'RTX', just change the expectation to whatever title you want)
 - Login (Set username and password on .env)
 - Save cookies
 - Unlock fast buy now option
 - Solev amazon captcha
 - Click on buy now
 - Make the purchase (Currently commented search for #.click() and uncommented to actually buy)
 - Log everything on discord
 - Script to make an automatic purchase on Amazon.com

## Known issues

  - Amazon recognizing bot: Must add proxy rotation, get proxies list in free proxy https://free-proxy-list.net/ and reload chrome driver every 30min or until failure.

## Requirements

- Python3 (but not supported v3.9 higher)
  - Selenium
  - dotenv

## How to run

※ Make sure you have 2FA (two factor authentication) turned off on your Amazon account!

### Copy and edit `.env` file

```
$ cp .env.sample .env
```

### Run

```
$ python3 main.py
```

Alternatively use Docker:

```
$ docker-compose build
$ docker-compose up -d
```

## License

Under MIT License.
