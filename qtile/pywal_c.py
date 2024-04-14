import json
from pathlib import Path

home = str(Path.home())

with open(home+'/.config/colours/tokyo.json','r') as colors_file:
    colors_dict = json.load(colors_file)

colors = list(colors_dict['colors'].values())
