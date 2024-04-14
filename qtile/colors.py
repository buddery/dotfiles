import json
import os

theme = 'city'

user = os.path.expanduser('~')

with open(user + "/.config/qtile/themes/" + theme + ".json") as theme_json:
    colors = json.load(theme_json)
