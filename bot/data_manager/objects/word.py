from bot.data_manager import db

from sqlitedict import SqliteDict
from bot.data_manager import config

table_name = "words"


class Word:
    text = ""
    xp = 0
    times_used = 0

    def __init__(self, text):
        self.text = text


def get_word(word):
    with SqliteDict("{0}.sqlite".format(config.get_database_name()), table_name) as words:
        data = words[word]
        return db.json_to_object(data)


def save_word(word):
    with SqliteDict("{0}.sqlite".format(config.get_database_name()), table_name) as words:
        words[word.text] = db.object_to_json(word)
        words.commit()

