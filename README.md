# Amazon Automation

Python script 

Set urls for products.

Login (Set username and password on .env)
Save cookies
Unlock fast buy now option
Solev amazon captcha
Click on buy now
Make the purchase
Log everything on discord
Script to make an automatic purchase on Amazon.com

---

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
