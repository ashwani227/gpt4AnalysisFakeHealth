import pandas as pd
import ast
import openai
import os
from dotenv import load_dotenv
import json
load_dotenv()


excel_file_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/FakeHealthNewsFullSet.xlsx'


# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)
matched = []
misMatched = []
for index, row in df.iterrows():
    # Accessing each element in the row
    review = row['Concise review']
    reviews = ast.literal_eval(review)
    gpt_output = row['GPT 4 output']
    index1 = 0
    # for item in reviews:

    all_question_response_list = gpt_output.split("\n\n")
    json_array = []
    for individual_question in all_question_response_list:
        single_question_response_list = individual_question.strip().split("\n")
        if len(single_question_response_list) > 1:
            responseString = " ".join(single_question_response_list[1:])
            if "not satisfactory" not in responseString.strip().lower():
                label = "Satisfactory"
            else:
                label = "Not satisfactory"
            json_array.append({
                "question": single_question_response_list[0],
                "response": single_question_response_list[1],
                "label": label
            })
    for review in reviews:
        for json_obj in json_array:
            if(review['question'].strip().lower()==json_obj['question'].strip().lower()):
                if review['answer'].strip().lower() == json_obj['label'].strip().lower():
                    matched.append({"gpt_label":json_obj['label'],"news_id": row['Index'],"question": json_obj['question'], "reviewer_label": review["answer"], "reviewer_explanation": review["explanation"], "description": row['Description'], "gpt_response": json_obj['response']})
                else:
                    misMatched.append({"gpt_label":json_obj['label'],"news_id": row['Index'],"question": json_obj['question'], "reviewer_label": review["answer"], "reviewer_explanation": review["explanation"], "description": row['Description'],"gpt_response": json_obj['response']})

    # print("Matched",matched)

    # print("\n misMatched", misMatched)
    # val = output_values[index1].strip()
    # labels = val.split("\n")
  
        # if label =='':
        # #     label = val.split(".")[-2]
        # question = item['question'].strip()  
        # my_labels = []
        # for label in labels:
        #     if label.strip().lower() != question.lower():
        #         my_labels.append(label)
        # if question in questions and my_labels not in questions[question]:
        #     if  not any ("not satisfactory" in label1.lower() for label1 in my_labels):
        #         # print(my_labels)
        #         questions[question].append([my_labels,row['Index'],item['explanation'] ,row['Description']])
        # else:
        #     try:
        #         if  not any ("not satisfactory" in label1.lower() for label1 in my_labels):
        #             # print(my_labels)

        #             questions[question] = [[my_labels,row['Index'],item['explanation'], row['Description']]]
        #             # questions[question] = [[my_labels,row['Index'],item['explanation']]]
        #     except:
        #         pass
        # index1+=1
        # print(index1)
        # if index1==6:
        #     break
    
    
# print(questions.keys())
# print(originalCount)
# for key, val in questions.items():
#     print(key, len(val))
# filename = "output_8.json"

# # Write the dictionary to a JSON file
# with open(filename, 'w') as json_file:
#     json.dump(questions, json_file)

# print(f"Data has been written to {filename}")
filename_mismatched = "misMatched.json"
filename_matched = "matched.json"


# Write the dictionary to a JSON file
with open(filename_mismatched, 'w') as json_file:
    json.dump(misMatched, json_file)

print(f"Data has been written to {filename_mismatched}")

with open(filename_matched, 'w') as json_file:
    json.dump(matched, json_file)

print(f"Data has been written to {filename_matched}")