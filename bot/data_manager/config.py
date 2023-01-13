import json


def get_openai_key():
    f = open('bot/data_manager/config.json')
    return json.load(f)["APIKeys"]["OpenAIAPIKey"]


def get_discord_key():
    f = open('bot/data_manager/config.json')
    return json.load(f)["APIKeys"]["DiscordApiKey"]


def get_role_channel():
    f = open('bot/data_manager/config.json')
    return json.load(f)["Channels"]["Roles"]


def get_database_name():
    f = open('bot/data_manager/config.json')
    return json.load(f)["Database"]["Name"]
