import json
import pandas as pd

# Load data from the JSON file
with open('matchedQuestions.json', 'r') as json_file:
    data = json.load(json_file)

with pd.ExcelWriter('Supplementary Table 4_ GPT not detected.xlsx') as writer:
    for key, value in data.items():
        print(key)
        df = pd.DataFrame(value, columns=[f"Column{i+1}" for i in range(len(value[0]))])
        sheet_name = key[22:50].replace('[', '').replace(']', '').replace('/', '_').replace('?', '_')
        df.to_excel(writer, sheet_name=sheet_name, index=False)