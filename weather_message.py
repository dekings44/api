import requests



parameter = {
    'lat': 54.760731,
    'lon': -1.332580,
    'appid': '4c126a2ed7a44edc6dcc5892054aae2f'
}


response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameter)

data = response.json()
print(data)
