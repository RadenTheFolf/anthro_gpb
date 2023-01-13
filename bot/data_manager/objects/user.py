import json


from sqlitedict import SqliteDict
from collections import namedtuple
from json import JSONEncoder
from bot.data_manager import config

table_name = "users"


class AGPBUser:
    UID = ""
    JOIN_DATE = ""
    NAME = ""
    NICK = ""
    XP = 0
    LEVEL = 0
    BAN_HISTORY = []
    WARN_HISTORY = []
    IS_ACTIVE = True
    LAST_ACTIVE_DATETIME = 0
    MESSAGES_SENT = 1
    ROLES = []
    MODERATION_LEVEL = 0

    def __init__(self, uid, name, nick, join_date):
        self.NAME = name
        self.UID = uid
        self.NICK = nick
        self.JOIN_DATE = join_date


class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def user_decoder(user_dict):
    return namedtuple('X', user_dict.keys())(*user_dict.values())


def json_to_user(data):
    return json.loads(data, object_hook=user_decoder)


def user_to_json(user):
    return json.dumps(user, indent=4, cls=UserEncoder)


def get_user(uid):
    with SqliteDict("{0}.sqlite".format(config.get_database_name()), table_name) as users:
        user = users[uid]
        return json_to_user(user)


def save_user(user: AGPBUser):
    with SqliteDict("{0}.sqlite".format(config.get_database_name()), table_name) as users:
        users[user.UID] = user_to_json(user)
        users.commit()
