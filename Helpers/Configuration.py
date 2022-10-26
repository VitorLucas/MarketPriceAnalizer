import json
import pathlib

with open("configuration.json", "r") as configurations:
    config = json.load(configurations)