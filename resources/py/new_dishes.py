import os
import json


# Define directory and file paths
directory = "json"
file_path = os.path.join(directory, "new_dishes.json")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


# Define menu items

menu_items = [
  {"number": "N7","title": "Nigiri Tofu","pieces": "2 Peças" ,"image": "resources/img/N7.jpg"},
  {"number": "N13","title": "Tofu c/ Frutas","pieces": "2 Peças" ,"image": "resources/img/N13.jpg"},
  {"number": "N23","title": "Queijo c/ Frutas","pieces": "2 Peças" ,"image": "resources/img/N23.jpg"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)