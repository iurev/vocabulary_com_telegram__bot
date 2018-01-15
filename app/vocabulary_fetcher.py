import requests
from bs4 import BeautifulSoup
from app.config import config as _conf

config = _conf["vocabulary"]


def request():
    return requests.get(
        config["mastered_words_url"],
        headers=config["headers"],
        cookies=config["cookies"]
    )


def process(page):
    soup = BeautifulSoup(page, "html.parser")
    words = []
    for html_word in soup.find("ol", attrs={"class": "words"}).find_all("a"):
        words.append({
            "value": html_word.find("span").text,
            "definition": html_word.find("dfn").text,
            "link": html_word.get("href")
        })
    return words


def get_mastered_words():
    response = request()
    return process(response.text)
