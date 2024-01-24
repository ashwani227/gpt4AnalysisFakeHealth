import json

json_file_path = "output.json"

# Read the JSON file
with open(json_file_path, "r") as file:
    data = json.load(file)

for key,values in data.items():
    count = 0
    
    # values = list(set(values))
    for value in values:
        if "not satisfactory" in value[0].lower():
            count +=1
            # print(key, value[0])
    print(key, count)

# Does the news release adequately discuss the costs of the intervention? 459
# Does the news release adequately quantify the benefits of the treatment/test/product/procedure? 369
# Does the news release adequately explain/quantify the harms of the intervention? 388
# Does the news release seem to grasp the quality of the evidence?  374
# Does the news release include unjustifiable, sensational language, including in the quotes of researchers? 194
# Does the news release identify funding sources & disclose conflicts of interest? 270
# Does the news release establish the availability of the treatment/test/product/procedure? 182
# Does the news release establish the true novelty of the approach? 190
# Does the news release compare the new approach with existing alternatives? 280
# Does the news release commit disease-mongering? 68


# {'Does the news release adequately discuss the costs of the intervention?': 489, 
#  'Does the news release adequately quantify the benefits of the treatment/test/product/procedure?': 443,
#    'Does the news release adequately explain/quantify the harms of the intervention?': 449, 
#    'Does the news release seem to grasp the quality of the evidence? ': 442, 
#    'Does the news release include unjustifiable, sensational language, including in the quotes of researchers?': 230, 
#    'Does the news release identify funding sources & disclose conflicts of interest?': 316, 
#    'Does the news release establish the availability of the treatment/test/product/procedure?': 199, 
#    'Does the news release establish the true novelty of the approach?': 227,
#      'Does the news release compare the new approach with existing alternatives?': 331, 
#  'Does the news release commit disease-mongering?': 72}