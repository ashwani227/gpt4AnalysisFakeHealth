import json
import os

# Specify the path to the folder containing your JSON files
folder_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/dataset/content/HealthStory'

# Specify the output file where you want to merge the JSON data
output_file_path = 'C:/Users/ashwa/Desktop/llm/FakeHealth/dataset/content/merged.json'

# Initialize an empty list to store the data from all JSON files
merged_data = []

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        # Read data from each JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            filename = filename[:-5]
            # Append data to the merged_data list
            merged_data.append({filename:data})

# Write the merged data to the output file
with open(output_file_path, 'w') as output_file:
    json.dump(merged_data, output_file, indent=2)

print(f'Merged data written to {output_file_path}')
