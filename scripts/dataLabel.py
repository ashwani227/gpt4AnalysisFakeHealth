import pandas as pd
import ast
import openai
import os
from dotenv import load_dotenv
import json
load_dotenv()

# openai.organization = "org-EV9FFMQ9dOPFnlDlIsJwaP6i"
# openai.api_key = os.getenv("OPENAI_API_KEY")

excel_file_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/FakeHealthNewsFullSet.xlsx'


# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)
review_c = []
gpt_outputs = []
record_count = 0
questions = {}
originalCount = {}

for index, row in df.iterrows():
    # Accessing each element in the row
    gpt_prompt = ""
    review = row['Concise review']
    reviews = ast.literal_eval(review)
    output = row['GPT 4 output']
    index1 = 0
    for item in reviews:
        # if item['question'] in originalCount:
        #     originalCount[item['question']] +=1
        # else:
        #     originalCount[item['question']] = 1
        output_values = output.split("\n\n")
        val = output_values[index1].strip()
        labels = val.split("\n")
        # if label =='':
        #     label = val.split(".")[-2]
        question = item['question'].strip()  
        my_labels = []
        for label in labels:
            if label.strip().lower() != question.lower():
                my_labels.append(label)
        if question in questions and my_labels not in questions[question]:
            if  not any ("not satisfactory" in label1.lower() for label1 in my_labels):
                # print(my_labels)
                questions[question].append([my_labels,row['Index'],item['explanation'] ,row['Description']])
        else:
            try:
                if  not any ("not satisfactory" in label1.lower() for label1 in my_labels):
                    # print(my_labels)

                    questions[question] = [[my_labels,row['Index'],item['explanation'], row['Description']]]
                    # questions[question] = [[my_labels,row['Index'],item['explanation']]]
            except:
                pass
        index1+=1
        print(index1)
        if index1==6:
            break
    
    
# print(questions.keys())
# print(originalCount)
# for key, val in questions.items():
#     print(key, len(val))
# filename = "output_8.json"

# # Write the dictionary to a JSON file
# with open(filename, 'w') as json_file:
#     json.dump(questions, json_file)

# print(f"Data has been written to {filename}")