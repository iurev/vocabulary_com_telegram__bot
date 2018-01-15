# Vocabulary.com telegram bot

The bot reminds last learned words like this:

<img width="570" alt="screen shot 2018-01-15 at 16 01 38" src="https://user-images.githubusercontent.com/3179564/34943637-8449097e-fa0d-11e7-9d82-06645100712d.png">

## How to run

```
git clone https://github.com/wwju/vocabulary_com_telegram__bot.git
cd vocabulary_com_telegram__bot
cp config/default.yml config/private.yml
# Setup your creditials for telegram and vocabulary.com in config.private.yml
docker-compose build
bin/app
```

## How to get vocabulary.com creditials

Unfortunatelly, it doesn't support API, so this bot uses scapes HTML using cookies from your account.

1. Go to vocabulary.com with openned network inspector
2. Copy first request cURL
3. Insert data in config/private.yml

Also, look here [curl.trillworks.com](https://curl.trillworks.com)
