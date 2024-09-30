# -*- coding: utf-8 -*-
import json
import re

with open("FilterDictionary.json", "r", encoding='utf-8') as filters:
    filters = json.load(filters)

class Filter:

    @classmethod
    def filter_expression(self, sting_to_substitute):
        return  self.replace_string(sting_to_substitute, "expressions")

    # @classmethod
    # def filter_char(self, sting_to_substitute):
    #     return self.replace_string(sting_to_substitute, "char")

    @classmethod
    def filter_price(self, sting_to_substitute):
        return self.replace_string(sting_to_substitute, "price")

    @classmethod
    def replace_string(self, sting_to_substitute, select_dictionary):
        for filter in filters[select_dictionary]:
            if select_dictionary == "price" and filter["pattern"] == "Quilograma":
                return float(re.sub(filter["pattern"], '', sting_to_substitute, flags=re.IGNORECASE).strip())

            sting_to_substitute = re.sub(filter["pattern"], filter["replacment"], sting_to_substitute,flags=re.IGNORECASE)
        return sting_to_substitute