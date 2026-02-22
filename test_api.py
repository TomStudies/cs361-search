import requests
import json

BASE_URL = "http://127.0.0.1:8000/search/"

search_terms = ["cat", "mustard", "6", "fiend"]

# Two sample data sets (data may be in any format, so long as it is a list of json objects)
data_set_1 = [
  {"name": "Martin", "species": "fish"},
  {"name": "Carlos", "species": "dog"},
  {"name": "Fred", "species": "cat"},
  {"name": "Friend", "species": "fish"}
]

data_set_2 = [
    {"brand": "Ford", "model": "Taurus", "year": 1992},
    {"brand": "Ford", "model": "Mustang", "year": 1964},
    {"brand": "Chevrolet", "model": "Corvette", "year": 1953},
    {"brand": "Buick", "model": "Wildcat", "year": 1968}
]

# Conduct an example search for each term across both data sets
for term in search_terms:
    print(f"Searching for {term}:")

    # Construct the URL with the search term
    url = f"{BASE_URL}{term}"

    # Send the post request for the first data set
    response = requests.post(url, json=data_set_1)

    if response.status_code == 200:
        # If successful, display sorted results
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    print("\n")

    # Send the post request for the second data set
    response = requests.post(url, json=data_set_2)

    if response.status_code == 200:
        # If successful, display sorted results
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    print("\n")



