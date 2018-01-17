from app import telegram, view, vocabulary_fetcher
import os
import schedule
import time


def job():
    words = vocabulary_fetcher.get_mastered_words()
    message = view.format(words[:10])
    telegram.send(message)

schedule.every().day.at(os.environ["TIME_TO_SEND"]).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
