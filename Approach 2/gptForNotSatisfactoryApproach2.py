import pandas as pd
import ast
import openai
import os
from dotenv import load_dotenv
import math
load_dotenv()

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

excel_file_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/FakeHealthNewsFullSet.xlsx'

def getGPTOutput(gpt_prompt):
    message=[{"role": "user", "content": gpt_prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.2,
        frequency_penalty=0.0)
    return response['choices'][0]['message']['content']

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)
review_c = []
gpt_outputs = []
record_count = 0

for index, row in df.iterrows():
    # Accessing each element in the row
    gpt_prompt = ""
    review = row['Review']
    reviews = ast.literal_eval(review)
    concise_review = []
    questions = ""
    for item in reviews:
        if item['answer'] == "Not Satisfactory":
            concise_review.append(item)
            questions+=(item['question'])
    paragraphs = row['Description'].split('\n\n', 1)
    claim = paragraphs[0]
    study = (" ").join(paragraphs[1:])
    study = study.replace('\n',' ')
    gpt_prompt+= claim + study  +"\n"+questions + "Can you assign an overall label such as Satisfactory or Not satisfactory to this data based on the questions? Also, give your justification for the answer to the questions? Also, create a separate response for each of the question and add a Satisfactory or Not satisfactory label for each question as well?"
    print("processing", record_count)
    gpt4Exists = row['GPT 4 output']
    if pd.notna(gpt4Exists) and gpt4Exists != '':
        
        gpt4Value = gpt4Exists
    else:
        gpt4Value = getGPTOutput(gpt_prompt)
    record_count+=1
    review_c.append(concise_review)
    gpt_outputs.append(gpt4Value)
        # df.at[index, 'Concise Review'] = concise_review
    df.at[index, 'GPT 4 output'] = gpt4Value
    
    
    # Write the updated DataFrame to the Excel file
    output_excel_file_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/FakeHealthNewsFullSet.xlsx'
    df.to_excel(output_excel_file_path, index=False)
    
#     print(f"\nRow {index} processed. DataFrame has been updated and written to {output_excel_file_path}")
df['Concise review'] = review_c
df.to_excel(output_excel_file_path, index=False)    
print(f"\nRow {index} processed. DataFrame has been updated and written to {output_excel_file_path}")