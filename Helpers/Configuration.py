import json
import pathlib

with open("configuration.json", "r") as configurations:
    config = json.load(configurations)

with open("products.json", "r") as product_list:
    product_list = json.load(product_list)