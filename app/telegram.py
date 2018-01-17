import telegram
import os

bot = telegram.Bot(os.environ["TELEGRAM_KEY"])


def send(text):
    bot.sendMessage(
        chat_id=os.environ["TELEGRAM_ME_ID"],
        text=text,
        parse_mode=telegram.ParseMode.MARKDOWN
    )
