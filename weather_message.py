import requests
import pandas as pd
import numpy as np


# parameter = {
#     'lat': 54.760731,
#     'lon': -1.332580,
#     'appid': '4c126a2ed7a44edc6dcc5892054aae2f'
# }


# response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameter)

# data = response.json()
# print(data)

uk_data = pd.read_csv('uk_cities.csv')
uk_data["Latitude"] = pd.to_numeric(uk_data["Latitude"], downcast="float")
uk_data["Longitude"] = pd.to_numeric(uk_data["Longitude"], downcast="float")





parameter = {
    'lat': uk_data["Latitude"].to_list(),
    'lon': uk_data["Longitude"].to_list(),
    'appid': 'b47e8de2d33cf04a255c63b07998720f'
}


response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)

data_first = response.json()['list'][0]
data_second = response.json()['list'][1]
data_third = response.json()['list'][2]
data_fourth = response.json()['list'][3]

weather_next_3hrs_list = []
weather_desc_next_3hrs_list = []
date_time_next_3hrs_list = []

weather_next_6hrs_list = []
weather_desc_next_6hrs_list = []
date_time_next_6hrs_list = []

weather_next_9hrs_list = []
weather_desc_next_9hrs_list = []
date_time_next_9hrs_list = []

weather_next_12hrs_list = []
weather_desc_next_12hrs_list = []
date_time_next_12hrs_list = []

for index, row in uk_data.iterrows():
    # Extract the value from the current row
    parameter = {
    'lat': row["Latitude"],
    'lon': row["Longitude"],
    'appid': 'b47e8de2d33cf04a255c63b07998720f'
    }

    # Send the API request
    response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)
    data_first = response.json()['list'][0]
    weather_next_3hrs = data_first['weather'][0]['main']
    weather_desc_next_3hrs = data_first['weather'][0]['description']
    date_time_next_3hrs = data_first['dt_txt']

    # Append the values to the respective lists
    weather_next_3hrs_list.append(weather_next_3hrs)
    weather_desc_next_3hrs_list.append(weather_desc_next_3hrs)
    date_time_next_3hrs_list.append(date_time_next_3hrs)

    #Getting the second item
    data_second = response.json()['list'][1]
    weather_next_6hrs = data_second['weather'][0]['main']
    weather_desc_next_6hrs = data_second['weather'][0]['description']
    date_time_next_6hrs = data_second['dt_txt']

    # Append the values to the respective lists
    weather_next_6hrs_list.append(weather_next_6hrs)
    weather_desc_next_6hrs_list.append(weather_desc_next_6hrs)
    date_time_next_6hrs_list.append(date_time_next_6hrs)

    #Getting the third item
    data_third = response.json()['list'][2]
    weather_next_9hrs = data_third['weather'][0]['main']
    weather_desc_next_9hrs = data_third['weather'][0]['description']
    date_time_next_9hrs = data_third['dt_txt']

    # Append the values to the respective lists
    weather_next_9hrs_list.append(weather_next_9hrs)
    weather_desc_next_9hrs_list.append(weather_desc_next_9hrs)
    date_time_next_9hrs_list.append(date_time_next_9hrs)

    #Getting the second item
    data_fourth = response.json()['list'][3]
    weather_next_12hrs = data_fourth['weather'][0]['main']
    weather_desc_next_12hrs = data_fourth['weather'][0]['description']
    date_time_next_12hrs = data_fourth['dt_txt']

    # Append the values to the respective lists
    weather_next_12hrs_list.append(weather_next_12hrs)
    weather_desc_next_12hrs_list.append(weather_desc_next_12hrs)
    date_time_next_12hrs_list.append(date_time_next_12hrs)
    



# weather_next_6hrs = pd.Series([weather for weather in data_second['weather'][0]['main']])
# weather_desc_next_6hrs = pd.Series([weatherdesc for weatherdesc in data_second['weather'][0]['description']])
# date_time_next_6hrs = pd.Series([date_time for date_time in data_second['dt_txt']])

# weather_next_9hrs = pd.Series([weather for weather in data_third['weather'][0]['main']])
# weather_desc_next_9hrs = pd.Series([weatherdesc for weatherdesc in data_third['weather'][0]['description']])
# date_time_next_9hrs = pd.Series([date_time for date_time in data_third['dt_txt']])

# weather_next_12hrs = pd.Series([weather for weather in data_fourth['weather'][0]['main']])
# weather_desc_next_12hrs = pd.Series([weatherdesc for weatherdesc in data_fourth['weather'][0]['description']])
# date_time_next_12hrs = pd.Series([date_time for date_time in data_fourth['dt_txt']])

uk_data["weather_next_3hrs"] = weather_next_3hrs_list
uk_data["weather_desc_next_3hrs"] = weather_desc_next_3hrs_list
uk_data["date_time_next_3hrs"] = date_time_next_3hrs_list

uk_data["weather_next_6hrs"] = weather_next_6hrs_list
uk_data["weather_desc_next_6hrs"] = weather_desc_next_6hrs_list
uk_data["date_time_next_6hrs"] = date_time_next_6hrs_list

uk_data["weather_next_9hrs"] = weather_next_9hrs_list
uk_data["weather_desc_next_9hrs"] = weather_desc_next_9hrs_list
uk_data["date_time_next_9hrs"] = date_time_next_9hrs_list

uk_data["weather_next_12hrs"] = weather_next_12hrs_list
uk_data["weather_desc_next_12hrs"] = weather_desc_next_12hrs_list
uk_data["date_time_next_12hrs"] = date_time_next_12hrs_list

print(uk_data.head(10))
uk_data.to_csv('ukweather.csv')






# print(f'The current weather detail: It is {weather_next_3hrs}, and {weather_desc_next_3hrs} during {date_time_next_3hrs}')
# print(f'The current weather detail: It is {weather_next_6hrs}, and {weather_desc_next_6hrs} during {date_time_next_6hrs}')
# print(f'The current weather detail: It is {weather_next_9hrs}, and {weather_desc_next_9hrs} during {date_time_next_9hrs}')
# print(f'The current weather detail: It is {weather_next_12hrs}, and {weather_desc_next_12hrs} during {date_time_next_12hrs}')



