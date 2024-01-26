import json
import openai
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

script_directory = os.path.dirname(os.path.abspath(__file__))

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

def getGPTOutput(gpt_prompt):
    message=[{"role": "user", "content": gpt_prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.2,
        frequency_penalty=0.0)
    return response['choices'][0]['message']['content']

json_file_path = os.path.join(script_directory, '../../dataset/HealthRelease.json')
file_path = os.path.join(script_directory, '../Output Data/FakeHealthRelease.xlsx')
folder_path = os.path.join(script_directory, '../../dataset/HealthRelease')

# Read the Excel file into a pandas DataFrame
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

query = "Analyze the following text and find misleading information in it. Only show the results for which you have references for your claims. Also, it would be good if you can assign a label - True or false in the front if there is any misleading information. The text is: "

record_count = 0
try:
    df_existing = pd.read_excel(file_path)
except FileNotFoundError:
    # If the file doesn't exist, create a new DataFrame with headers
    df_existing = pd.DataFrame(columns=['Index', 'Url', 'Source Url','Title','Description','Review','GPT 4'])  # Add your column names

for item in json_data:
    file_path_json = os.path.join(folder_path, (item['news_id'] + ".json"))
    # Read data from each JSON file
    try:
        with open(file_path_json, 'r') as file:
            data = json.load(file)
            description = data['text']
    except:
        continue
    try:
        gpt4Value = getGPTOutput(query + description)
        new_record = [item['news_id'],item['link'],item['source_link'],item['title'],description,gpt4Value,item['criteria']]
        # Create a DataFrame with the new record
        df_new = pd.DataFrame([new_record], columns=['Index', 'Url', 'Source Url','Title','Description','GPT 4','Review'])  # Adjust column names

        if record_count == 0:
            df_combined = df_existing.copy()
        else:
            df_combined = pd.concat([df_combined, df_new], ignore_index=True)
        print(record_count)
        # Write the combined DataFrame back to the Excel file periodically
        if record_count % 10== 0:  # Adjust the frequency of saving as needed
            df_combined.reset_index(drop=True, inplace=True)  # Reset index before saving
            df_combined.to_excel(file_path, index=False)
            df_existing = df_combined.copy()  # Update existing DataFrame for the next iteration
        record_count += 1

    except Exception as e:
        print(f"Error: {e}")
        # Handle the error as needed (e.g., log the error, skip the record, etc.)

# Save the remaining data at the end
df_combined.reset_index(drop=True, inplace=True)  # Reset index before saving
df_combined.to_excel(file_path, index=False)
print("Data appended successfully.")