import telegram
from app.config import config

bot = telegram.Bot(config["telegram"]["key"])


def send(text):
    bot.sendMessage(
        chat_id=config["telegram"]["me_id"],
        text=text,
        parse_mode=telegram.ParseMode.MARKDOWN
    )
