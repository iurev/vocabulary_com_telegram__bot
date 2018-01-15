from app.config import config


def format(words):
    result = "*Your last mastered words:*\n"
    result += "```\n"
    for word in words:
        result += "{} – {} \n".format(
            word["value"],
            word["definition"]
        )
    result += "```"
    return result
