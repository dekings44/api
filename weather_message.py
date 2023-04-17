import requests



# parameter = {
#     'lat': 54.760731,
#     'lon': -1.332580,
#     'appid': '4c126a2ed7a44edc6dcc5892054aae2f'
# }


# response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameter)

# data = response.json()
# print(data)



parameter = {
    'lat': 54.760731,
    'lon': -1.332580,
    'appid': 'b47e8de2d33cf04a255c63b07998720f'
}


response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)

data_first = response.json()['list'][0]
data_second = response.json()['list'][1]
data_third = response.json()['list'][2]
data_fourth = response.json()['list'][3]
print(data_fourth)



