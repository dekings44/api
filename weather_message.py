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

weather_next_3hrs = data_first['weather'][0]['main']
weather_desc_next_3hrs = data_first['weather'][0]['description']
date_time_next_3hrs = data_first['dt_txt']


weather_next_6hrs = data_second['weather'][0]['main']
weather_desc_next_6hrs = data_second['weather'][0]['description']
date_time_next_6hrs = data_second['dt_txt']

weather_next_9hrs = data_third['weather'][0]['main']
weather_desc_next_9hrs = data_third['weather'][0]['description']
date_time_next_9hrs = data_third['dt_txt']

weather_next_12hrs = data_fourth['weather'][0]['main']
weather_desc_next_12hrs = data_fourth['weather'][0]['description']
date_time_next_12hrs = data_fourth['dt_txt']



print(f'The current weather detail: It is {weather_next_3hrs}, and {weather_desc_next_3hrs} during {date_time_next_3hrs}')
print(f'The current weather detail: It is {weather_next_6hrs}, and {weather_desc_next_6hrs} during {date_time_next_6hrs}')
print(f'The current weather detail: It is {weather_next_9hrs}, and {weather_desc_next_9hrs} during {date_time_next_9hrs}')
print(f'The current weather detail: It is {weather_next_12hrs}, and {weather_desc_next_12hrs} during {date_time_next_12hrs}')



