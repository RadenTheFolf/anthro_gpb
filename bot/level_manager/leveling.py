from bot.data_manager import userdb, worddb


def get_level_from_xp(xp):
    xp_scale = 0.25
    growth_rate = 3
    return round(xp_scale*(xp ** (1/growth_rate)))


def message_value(content):
    xp_earned = 0
    if isinstance(content, str):
        words = content.split()
        for word in words:
            word_db = worddb.WordDB()
            word_xp = word_db.get_xp_value(word)
            if word_xp > 0:
                xp_earned += word_xp
            else:
                xp_earned += 0.1
        return xp_earned

def add_user_xp(user_obj, xp):
    users = userdb.find_user(user_obj.id)
    if len(users) > 0:
        for user in users:
            userdb.add_xp_to_user(user, xp)
    else:
        userdb.create_user(user_obj)
        add_user_xp(user_obj, xp)


def update_user_level(user_obj):
    users = userdb.find_user(user_obj.id)
    for user in users:
        current_level = get_level_from_xp(user.get("XP"))
        if user.get("LEVEL") < current_level:
            userdb.set_user_level(user, current_level)
            return True, current_level
        return False, current_level


images = [
    "",
    "https://i.imgur.com/EeE3sWA.png",
    "https://i.imgur.com/8p1eoHG.png",
    "https://i.imgur.com/18q0iVF.png",
    "https://i.imgur.com/6Kx5ZID.png",
    "https://i.imgur.com/yfkU1dy.png",
    "https://i.imgur.com/3GhRuJc.png",
    "https://i.imgur.com/0b1yeOX.png",
    "https://i.imgur.com/nwBGBq6.png",
    "https://i.imgur.com/lZ7Yhtx.png",
    "https://i.imgur.com/Fxmt0km.png",
    "https://i.imgur.com/NZ5TNXx.png",
    "https://i.imgur.com/KSN0mOl.png",
    "https://i.imgur.com/g7eecAn.png",
    "https://i.imgur.com/SFT6AZZ.png",
    "https://i.imgur.com/oHb8E4D.png",
    "https://i.imgur.com/08zP6sX.png",
    "https://i.imgur.com/v1z02IS.png",
    "https://i.imgur.com/m3VBmgO.png",
    "https://i.imgur.com/rwpbvx7.png",
    "https://i.imgur.com/TJaFnwD.png"
]