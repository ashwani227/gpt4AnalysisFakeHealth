import pandas as pd
import ast
from dotenv import load_dotenv
import json
load_dotenv()


excel_file_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/FakeHealthNewsFullSet.xlsx'


# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)
review_c = []
gpt_outputs = []
record_count = 0
questions = {}
originalCount = {}
myObj = {}

for index, row in df.iterrows():
    # Accessing each element in the row
    gpt_prompt = ""
    news_id = row['Index']
    output = row['GPT 4 output']
    stringObj = []
    output_values = output.split("\n")
    for out in output_values:
        label = out.rstrip()
        if "not satisfactory" not in label.lower() and "satisfactory" in label.lower():
            stringObj.append(label)
    myObj[news_id] = stringObj
    print(news_id)
# print(originalCount)
filename = "output2.json"

# Write the dictionary to a JSON file
with open(filename, 'w') as json_file:
    json.dump(myObj, json_file)

print(f"Data has been written to {filename}")