import json
import os
import sys
from datetime import datetime

# Define a Python dictionary
data = {
    "name": "John1221",
    "age": 30,
    "city": "New York",
    "created_at": str(datetime.now()) # Add current time to JSON data
}

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Define the path to the directory where the JSON file should be created
json_dir = os.path.join(script_dir, 'data')

# Create the directory if it doesn't exist
if not os.path.exists(json_dir):
    os.makedirs(json_dir)

# Define the file name with the current time included
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
json_filename = f"data_{current_time}.json"
json_path = os.path.join(json_dir, json_filename)

# Serialize the dictionary to a JSON string
json_data = json.dumps(data, indent=4)

# Write the JSON string to a file
with open(json_path, 'w') as f:
    f.write(json_data)

# Read the contents of the JSON file and print them
with open(json_path, 'r') as f:
    json_data = json.load(f)
    print(json_data)

# # Delete the JSON file
# os.remove(json_path)
# print("JSON file deleted successfully!")


print(script_dir)
print(json_path)
print(json_dir)