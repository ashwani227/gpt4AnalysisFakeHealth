import json
import pandas as pd
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
# Appending the relative path to the Excel file
json_file_name = os.path.join(script_directory, '../Output Data/matchedQuestions.json')
excel_file_path = os.path.join(script_directory, '../Output Data/Supplementary Table 4_ GPT not detected.xlsx')

# Load data from the JSON file
with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)

with pd.ExcelWriter(excel_file_path) as writer:
    for key, value in data.items():
        print(key)
        df = pd.DataFrame(value, columns=[f"Column{i+1}" for i in range(len(value[0]))])
        sheet_name = key[22:50].replace('[', '').replace(']', '').replace('/', '_').replace('?', '_')
        df.to_excel(writer, sheet_name=sheet_name, index=False)