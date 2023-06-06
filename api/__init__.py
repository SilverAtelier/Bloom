import os
import json


def get_key():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'key.json')
    with open(file_path, 'r') as f:
        return json.load(f)


__all__ = [get_key()]
