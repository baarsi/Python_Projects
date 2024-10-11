import requests

# Function to fetch data from the Star Wars API based on user input
def fetch_data(option):
    url = f"https://swapi.mimo.dev/api/{option}/"  # Constructing the API URL
    data = []
    
    try:
        # Sending the request to the API and getting the JSON data
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.HTTPError as e:
        # Handling HTTP errors (e.g., invalid requests or server issues)
        print(f"Error fetching data: {e}")
        return None

# Prompt user for API option (e.g., 'people', 'planets')
option = input("Enter an option (e.g., 'people' or 'planets'): ").strip().lower()
data = fetch_data(option)

# Print the names of the entities returned by the API (if any)
if data:
    for item in data:
        print(item["name"])
else:
    print("Unable to download data")
