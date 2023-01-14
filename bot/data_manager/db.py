import json

from collections import namedtuple
from json import JSONEncoder


class ObjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def object_decoder(user_dict):
    return namedtuple('X', user_dict.keys())(*user_dict.values())


def json_to_object(data):
    return json.loads(data, object_hook=object_decoder)


def object_to_json(user):
    return json.dumps(user, indent=4, cls=ObjectEncoder)
