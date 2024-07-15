import requests
from pprint import pprint
import json

# variable for the API url to check available categories
categories_url = "https://opentdb.com/api_category.php"

# variable for response from the API
response = requests.get(categories_url)

# pprint json response to see content in a readable format
pprint(response.json())

# write categories into a json file to use as reference in the main file for the app
with open("categories.json", "w") as f:
    json.dump(response.json(), f, indent=4)