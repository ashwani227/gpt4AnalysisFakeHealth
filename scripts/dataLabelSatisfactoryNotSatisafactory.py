import json

# Assuming your JSON file has a structure similar to this:
# [{"Index": 1, "GPT 4 output": "some output"}, {"Index": 2, "GPT 4 output": "another output"}, ...]
json_file_path = 'output.json'

# Read the JSON file into a list of dictionaries
with open(json_file_path, 'r') as json_file:
    data_list = json.load(json_file)

myObj = {}
for key,entry in data_list.items():
    print(key, len(entry))
    # print(entry)
    count = 0
    for out in entry:
        if(isinstance(out,list)):
            out = ", ".join(out)
        label = out.rstrip()
        if "not satisfactory" not in label.lower() and "satisfactory" in label.lower():
            count +=1
    print(count)  
    break

    # myObj[key] = count
    
    # news_id = entry['Index']
#     output = entry['GPT 4 output']
#     stringObj = []

#     output_values = output.split("\n")
#     for out in output_values:
#         label = out.rstrip()
#         if "not satisfactory" not in label.lower() and "satisfactory" in label.lower():
#             stringObj.append(label)

#     myObj[news_id] = stringObj
#     print(news_id)

# filename = "output2.json"

# # Write the dictionary to a JSON file
# with open(filename, 'w') as json_file:
#     json.dump(myObj, json_file, indent=2)  # Add indent=2 for pretty formatting

# print(f"Data has been written to {filename}")
print(myObj)