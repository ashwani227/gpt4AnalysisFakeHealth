import json
import pandas as pd

# Load data from the JSON file
with open('matchedQuestions.json', 'r') as json_file:
    data = json.load(json_file)
# with open('mismatchedQuestions.json', 'r') as json_file:
#     data = json.load(json_file)

# Create an Excel file with separate sheets for each key in the dictionary
# with pd.ExcelWriter('mismatchedFullSet.xlsx') as writer:
#     for key, value in data.items():
#         flattened_list = [item for sublist in value for item in sublist]
#         df = pd.DataFrame({key: flattened_list})
#         df.to_excel(writer, sheet_name=key[:30], index=False)

        # df = pd.DataFrame(value, columns=["news_id", "gpt_label", "reviewer_label", "reviewer_explanation", "gpt_reponse", "description"])
        # df.to_excel(writer, sheet_name=key, index=False)
# with pd.ExcelWriter('mismatchedQuestions.xlsx') as writer:
#     for key, value in data.items():
#         print(key)
#         df = pd.DataFrame(value, columns=[f"Column{i+1}" for i in range(len(value[0]))])
#         sheet_name = key[22:50].replace('[', '').replace(']', '').replace('/', '_').replace('?', '_')
#         df.to_excel(writer, sheet_name=sheet_name, index=False)

with pd.ExcelWriter('matchedQuestions.xlsx') as writer:
    for key, value in data.items():
        print(key)
        df = pd.DataFrame(value, columns=[f"Column{i+1}" for i in range(len(value[0]))])
        sheet_name = key[22:50].replace('[', '').replace(']', '').replace('/', '_').replace('?', '_')
        df.to_excel(writer, sheet_name=sheet_name, index=False)