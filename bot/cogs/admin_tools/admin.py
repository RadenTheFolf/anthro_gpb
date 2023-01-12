class AGPBBan:
    BAN_ID = ""
    BANNED_BY_ID = ""
    BANNED_BY_NAME = ""
    BAN_START_DATE = 0
    BAN_END_DATE = 0
    BAN_REASON = ""
    BAN_ACTIVE = False


class AGPBWarning:
    WARN_ID = ""
    WARNED_BY_ID = ""
    WANRNED_BY_NAME = ""
    WARN_DATETIME = 0
    WARN_REASON = ""
    PUNISHMENTS = []


class AGPBPunishment:
    NAME = ""
    DESCRIPTION = ""
    START_TIME = 0
    END_TIME = 0
    IS_ACTIVE = False
    Restrict = ""