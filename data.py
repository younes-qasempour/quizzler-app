import requests

API_URL = 'https://opentdb.com/api.php'
parameters = {
    'amount': '10',
    'type': 'boolean'
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()
data = response.json()['results']
question_data = data

