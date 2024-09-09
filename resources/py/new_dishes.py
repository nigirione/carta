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
  {"number": "80","title": "Califórnia de Gambas Panadas c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/N80.jpg"},
  {"number": "81","title": "Maki Frito c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/N81.jpg"},
  {"number": "82","title": "Califórnia Frito c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/N82.jpg"},
  {"number": "83","title": "Califórnia + Salmão Defumado c/ Molho de Frutas","pieces": "2 Peças" ,"image": "resources/img/N83.jpg"},
  {"number": "84","title": "Califórnia de Manga c/ Molho de Frutas","pieces": "4 Peças" ,"image": "resources/img/N84.jpg"},
  {"number": "85","title": "Sashimi Salmão c/ Molho de Frutas", "pieces": "5 Peças" ,"image": "resources/img/N85.jpg"},
  {"number": "86","title": "Gukan de Salmão Defumado c/ Molho","pieces": "2 Peças" ,"image": "resources/img/N86.jpg"},
]

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)