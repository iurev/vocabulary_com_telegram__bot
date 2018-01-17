import requests
from bs4 import BeautifulSoup
import os


def get_config(config_str):
    result = {}
    for line in config_str.split("\\n"):
        (key, val) = line.split(": ")
        result[key.replace("'", "")] = val.replace("'", "")
    return result


def request():
    return requests.get(
        os.environ["VOCABULARY_MASTERED_WORDS_URL"],
        headers=get_config(os.environ["VOCABULARY_HEADERS"]),
        cookies=get_config(os.environ["VOCABULARY_COOKIES"])
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
