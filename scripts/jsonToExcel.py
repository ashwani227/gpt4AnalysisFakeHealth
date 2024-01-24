import pandas as pd
import json
import os
# Specify the path to your JSON file
json_file_path = 'output_7.json'
excel_file_path = 'output_7.xlsx'

with open(json_file_path, 'r') as file:
    json_data = json.load(file)

if not os.path.isfile(excel_file_path):
    # If the file does not exist, create it with initial data or an empty DataFrame
    data_to_append= {
    'news_index': [],
    'gpt' : [],
    'expert' : [],
    'question':[],
    'description': []
    }
    initial_df = pd.DataFrame(data_to_append)

    # Write the initial DataFrame to the Excel file
    initial_df.to_excel(excel_file_path, index=False)
    print(f"File created: {excel_file_path}")

for key,values in json_data.items():
    for val in values:
        data_to_append['news_index'].append(val[1])
        data_to_append['expert'].append(val[2])
        data_to_append['gpt'].append(val[0])
        data_to_append['question'].append(key)
        data_to_append['description'].append(val[3])

df_to_append = pd.DataFrame(data_to_append)

# Read the existing Excel file
existing_df = pd.read_excel(excel_file_path)

# Append the new data to the existing DataFrame
updated_df = existing_df.append(df_to_append, ignore_index=True)

# Write the updated DataFrame to the same Excel file
updated_df.to_excel(excel_file_path, index=False)

print(f"Data successfully appended to {excel_file_path}")