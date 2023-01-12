from datetime import datetime

from tinydb import TinyDB, Query
import json

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
    MESSAGES_SENT = 0
    ROLES = []
    MODERATION_LEVEL = 0


USER_DB = "data/db/users.json"


def find_user(uid):
    db = TinyDB(USER_DB)
    user = Query()
    found = db.search(user.UID == uid)
    db.close()
    return found


def create_user(user):
    roles = []
    for role in user.roles:
        roles.append({
            "id": role.id,
            "name": role.name,
            "permissions": role.permissions.value
        })
    db = TinyDB(USER_DB)
    db.insert({
        "UID": user.id,
        "JOIN_DATE": user.joined_at.isoformat(),
        "NAME": user.name,
        "NICK": user.display_name,
        "XP": 0.0,
        "LEVEL": 0,
        "BAN_HISTORY": [],
        "WARN_HISTORY": [],
        "IS_ACTIVE": True,
        "LAST_ACTIVE_DATETIME": datetime.now().isoformat(),
        "MESSAGES_SENT": 1,
        "ROLES": roles,
        "MODERATION_LEVEL": 0
    })


def add_xp_to_user(user_obj, xp):
    current_xp = user_obj.get("XP")
    current_xp += xp
    db = TinyDB(USER_DB)
    user = Query()
    db.update({"XP": current_xp}, user.UID == user_obj.get("UID"))
    db.close()


def set_user_level(user_obj, level):
    db = TinyDB(USER_DB)
    user = Query()
    db.update({"LEVEL": level}, user.UID == user_obj.get("UID"))
    db.close()



