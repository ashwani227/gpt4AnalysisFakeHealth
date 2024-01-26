import pandas as pd
import json
import os
# Specify the path to your JSON file
script_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_directory, '../Output Data/mismatched.json')
question_based_file = os.path.join(script_directory, '../Output Data/mismatchedQuestions.json')
# json_file_path = 'matched.json'
# question_based_file = 'matchedQuestions.json'

with open(json_file_path, 'r') as file:
    json_data = json.load(file)
question_based_reponses = {}
for record in json_data:
    try: 
        if question_based_reponses[record['question'].strip()]:
            question_based_reponses[record['question'].strip()].append([record["news_id"],record['gpt_label'], record['reviewer_label'], record['gpt_response'], record['reviewer_explanation'], record["description"]]  )
    except:
        question_based_reponses[record['question'].strip()] = [[record["news_id"],record['gpt_label'], record['reviewer_label'], record['gpt_response'],record['reviewer_explanation'],record["description"]]]  


with open(question_based_file, 'w') as json_file:
    json.dump(question_based_reponses, json_file)

print(f"Data has been written to {question_based_file}")