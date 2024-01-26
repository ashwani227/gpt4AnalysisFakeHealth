import pandas as pd
import json
import os
# Specify the path to your JSON file
script_directory = os.path.dirname(os.path.abspath(__file__))
# Appending the relative path to the Excel file
json_file_path = os.path.join(script_directory, '../Output Data/mismatched.json')
question_based_file = os.path.join(script_directory, '../Output Data/numberOfReleaseFail.json')


with open(json_file_path, 'r') as file:
    json_data = json.load(file)
news_release = {}
keys = [0 for i in range(1,607)]

for record in json_data:
    try: 
        if news_release[record['news_id'].strip()]:
            news_release[record['news_id'].strip()] +=1
    except:
        news_release[record['news_id'].strip()] =1

    key_id = int(record['news_id'].split("news_reviews_")[1])
    keys[key_id] = 1
    
for index in range(len(keys)):
    if keys[index] == 0:
        if(index < 10):
            news_release["news_release_0000" + str(index)] = 0
        elif(index < 100):
            news_release["news_release_000" + str(index)] = 0
        else:
            news_release["news_release_00" + str(index)] = 0

valueBasedDict = {}
for key, val in news_release.items():
    try:
        valueBasedDict[val]+=1
    except:
        valueBasedDict[val] = 1
print(valueBasedDict)
with open(question_based_file, 'w') as json_file:
    json.dump(news_release, json_file)
