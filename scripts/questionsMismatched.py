import pandas as pd
import json
import os
# Specify the path to your JSON file
json_file_path = 'mismatched.json'
question_based_file = 'mismatchedQuestions.json'
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
#     initial_df = pd.DataFrame(data_to_append)

#     # Write the initial DataFrame to the Excel file
#     initial_df.to_excel(excel_file_path, index=False)
#     print(f"File created: {excel_file_path}")

# for key,values in json_data.items():
#     for val in values:
#         data_to_append['news_index'].append(val[1])
#         data_to_append['expert'].append(val[2])
#         data_to_append['gpt'].append(val[0])
#         data_to_append['question'].append(key)
#         data_to_append['description'].append(val[3])

# df_to_append = pd.DataFrame(data_to_append)

# # Read the existing Excel file
# existing_df = pd.read_excel(excel_file_path)

# # Append the new data to the existing DataFrame
# updated_df = existing_df.append(df_to_append, ignore_index=True)

# # Write the updated DataFrame to the same Excel file
# updated_df.to_excel(excel_file_path, index=False)

# print(f"Data successfully appended to {excel_file_path}")