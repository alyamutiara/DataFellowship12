import requests
import json

def fetch_and_save_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f'Data saved to {filename}')
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')

# Fetch users data
fetch_and_save_data('https://dummyjson.com/users', 'users.json')