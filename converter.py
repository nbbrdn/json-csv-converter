import os
import pandas as pd
import json
from pandas.io.json import json_normalize


def convert_to_csv(json):
    normalized_json = json_normalize(json)
    normalized_json.set_index('name', inplace=True)
    print(json)

    if os.path.exists("converted_csv_file.csv"):
        with open("converted_csv_file.csv", "a+") as file:
            normalized_json.to_csv(file, header=False)
    else:
        normalized_json.to_csv("converted_csv_file.csv")
    print("Converted nested json to normalized csv successfully")



''' Choose any json file to call the above method '''

with open("json_example.json", "r") as file:
    convert_to_csv(json.load(file))
