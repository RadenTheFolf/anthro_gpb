from bot.data_manager import db

from sqlitedict import SqliteDict
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


def get_user(uid) -> AGPBUser:
    with SqliteDict("{0}.sqlite".format(config.get_database_name()), table_name) as users:
        user = users[uid]
        return db.json_to_object(user)


def save_user(user: AGPBUser) -> None:
    with SqliteDict("{0}.sqlite".format(config.get_database_name()), table_name) as users:
        users[user.UID] = db.object_to_json(user)
        users.commit()
