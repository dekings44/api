import requests
import pandas as pd
import numpy as np
import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
open_weather_appid = os.environ['OPEN_WEATHER_APPID']
client = Client(account_sid, auth_token)


uk_data = pd.read_csv('uk_cities.csv')
uk_data["Latitude"] = pd.to_numeric(uk_data["Latitude"], downcast="float")
uk_data["Longitude"] = pd.to_numeric(uk_data["Longitude"], downcast="float")

weather_next_3hrs_list = []
weather_desc_next_3hrs_list = []
temp_next_3hrs_list = []
temp_feels_next_3hrs_list = []
date_time_next_3hrs_list = []

weather_next_6hrs_list = []
weather_desc_next_6hrs_list = []
temp_next_6hrs_list = []
temp_feels_next_6hrs_list = []
date_time_next_6hrs_list = []

weather_next_9hrs_list = []
weather_desc_next_9hrs_list = []
temp_next_9hrs_list = []
temp_feels_next_9hrs_list = []
date_time_next_9hrs_list = []

weather_next_12hrs_list = []
weather_desc_next_12hrs_list = []
temp_next_12hrs_list = []
temp_feels_next_12hrs_list = []
date_time_next_12hrs_list = []

for index, row in uk_data.iterrows():
    # Extract the value from the current row
    parameter = {
    'lat': row["Latitude"],
    'lon': row["Longitude"],
    'appid': open_weather_appid
    }

    # Send the API request
    response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)
    data_first = response.json()['list'][0]
    weather_next_3hrs = data_first['weather'][0]['main']
    weather_desc_next_3hrs = data_first['weather'][0]['description']
    temp_next_3hrs = data_first['main']['temp']
    temp_feels_next_3hrs = data_first['main']['feels_like']
    date_time_next_3hrs = data_first['dt_txt']

    # Append the values to the respective lists
    weather_next_3hrs_list.append(weather_next_3hrs)
    weather_desc_next_3hrs_list.append(weather_desc_next_3hrs)
    temp_next_3hrs_list.append(temp_next_3hrs)
    temp_feels_next_3hrs_list.append(temp_feels_next_3hrs)
    date_time_next_3hrs_list.append(date_time_next_3hrs)

    #Getting the second item
    data_second = response.json()['list'][1]
    weather_next_6hrs = data_second['weather'][0]['main']
    weather_desc_next_6hrs = data_second['weather'][0]['description']
    temp_next_6hrs = data_second['main']['temp']
    temp_feels_next_6hrs = data_second['main']['feels_like']
    date_time_next_6hrs = data_second['dt_txt']

    # Append the values to the respective lists
    weather_next_6hrs_list.append(weather_next_6hrs)
    weather_desc_next_6hrs_list.append(weather_desc_next_6hrs)
    temp_next_6hrs_list.append(temp_next_6hrs)
    temp_feels_next_6hrs_list.append(temp_feels_next_6hrs)
    date_time_next_6hrs_list.append(date_time_next_6hrs)

    #Getting the third item
    data_third = response.json()['list'][2]
    weather_next_9hrs = data_third['weather'][0]['main']
    weather_desc_next_9hrs = data_third['weather'][0]['description']
    temp_next_9hrs = data_third['main']['temp']
    temp_feels_next_9hrs = data_third['main']['feels_like']
    date_time_next_9hrs = data_third['dt_txt']

    # Append the values to the respective lists
    weather_next_9hrs_list.append(weather_next_9hrs)
    weather_desc_next_9hrs_list.append(weather_desc_next_9hrs)
    temp_next_9hrs_list.append(temp_next_9hrs)
    temp_feels_next_9hrs_list.append(temp_feels_next_9hrs)
    date_time_next_9hrs_list.append(date_time_next_9hrs)

    #Getting the fourth item
    data_fourth = response.json()['list'][3]
    weather_next_12hrs = data_fourth['weather'][0]['main']
    weather_desc_next_12hrs = data_fourth['weather'][0]['description']
    temp_next_12hrs = data_fourth['main']['temp']
    temp_feels_next_12hrs = data_fourth['main']['feels_like']
    date_time_next_12hrs = data_fourth['dt_txt']

    # Append the values to the respective lists
    weather_next_12hrs_list.append(weather_next_12hrs)
    weather_desc_next_12hrs_list.append(weather_desc_next_12hrs)
    temp_next_12hrs_list.append(temp_next_12hrs)
    temp_feels_next_12hrs_list.append(temp_feels_next_12hrs)
    date_time_next_12hrs_list.append(date_time_next_12hrs)

uk_data["weather_next_3hrs"] = weather_next_3hrs_list
uk_data["weather_desc_next_3hrs"] = weather_desc_next_3hrs_list
uk_data["temp_next_3hrs"] = temp_next_3hrs_list
uk_data["temp_feels_next_3hrs"] = temp_feels_next_3hrs_list
uk_data["date_time_next_3hrs"] = date_time_next_3hrs_list

uk_data["weather_next_6hrs"] = weather_next_6hrs_list
uk_data["weather_desc_next_6hrs"] = weather_desc_next_6hrs_list
uk_data["temp_next_6hrs"] = temp_next_6hrs_list
uk_data["temp_feels_next_6hrs"] = temp_feels_next_6hrs_list
uk_data["date_time_next_6hrs"] = date_time_next_6hrs_list

uk_data["weather_next_9hrs"] = weather_next_9hrs_list
uk_data["weather_desc_next_9hrs"] = weather_desc_next_9hrs_list
uk_data["temp_next_9hrs"] = temp_next_9hrs_list
uk_data["temp_feels_next_9hrs"] = temp_feels_next_9hrs_list
uk_data["date_time_next_9hrs"] = date_time_next_9hrs_list

uk_data["weather_next_12hrs"] = weather_next_12hrs_list
uk_data["weather_desc_next_12hrs"] = weather_desc_next_12hrs_list
uk_data["temp_next_12hrs"] = temp_next_12hrs_list
uk_data["temp_feels_next_12hrs"] = temp_feels_next_12hrs_list
uk_data["date_time_next_12hrs"] = date_time_next_12hrs_list

new_data = uk_data.loc[(uk_data['Place Name'] == 'Newcastle Upon Tyne, the UK') | (uk_data['Place Name'] == 'Durham, the UK')]

temp_6hr = new_data.iloc[0]['temp_next_6hrs']
feels_6hr = new_data.iloc[0]['temp_feels_next_6hrs']
place = new_data.iloc[0]['Place Name']
time_6hr = new_data.iloc[0]['date_time_next_6hrs']
weather_6hr = new_data.iloc[0]['weather_next_6hrs']
weather_desc_6hr = new_data.iloc[0]['weather_desc_next_6hrs']

temp_9hr = new_data.iloc[0]['temp_next_9hrs']
feels_9hr = new_data.iloc[0]['temp_feels_next_9hrs']
time_9hr = new_data.iloc[0]['date_time_next_9hrs']
weather_9hr = new_data.iloc[0]['weather_next_9hrs']
weather_desc_9hr = new_data.iloc[0]['weather_desc_next_9hrs']

temp_6hr_1 = new_data.iloc[1]['temp_next_6hrs']
feels_6hr_1 = new_data.iloc[1]['temp_feels_next_6hrs']
place_1 = new_data.iloc[1]['Place Name']
time_6hr_1 = new_data.iloc[1]['date_time_next_6hrs']
weather_6hr_1 = new_data.iloc[1]['weather_next_6hrs']
weather_desc_6hr_1 = new_data.iloc[1]['weather_desc_next_6hrs']

temp_9hr_1 = new_data.iloc[1]['temp_next_9hrs']
feels_9hr_1 = new_data.iloc[1]['temp_feels_next_9hrs']
time_9hr_1 = new_data.iloc[1]['date_time_next_9hrs']
weather_desc_9hr_1 = new_data.iloc[1]['weather_next_9hrs']
weather_9hr_1 = new_data.iloc[1]['weather_desc_next_9hrs']

message_rain = f'Place: {place}\n Time: {time_6hr}\n Temperature: {temp_6hr}\n Feels like: {feels_6hr}\n The weather is {weather_desc_6hr}\n\n\n Time: {time_9hr}\n Temperature: {temp_9hr}\n Feels like: {feels_9hr}\n The weather is {weather_desc_9hr}\n -----------------------------\n\n Place: {place_1}\n Time: {time_6hr_1}\n Temperature: {temp_6hr_1}\n Feels like: {feels_6hr_1}\n The weather is {weather_desc_6hr_1}\n\n\n Time: {time_9hr_1}\n Temperature: {temp_9hr_1}\n Feels like: {feels_9hr_1}\n The weather is {weather_desc_9hr_1}. \n\nIt seems it is going to rain today, you may need an ☂️'
message = f'Place: {place}\n Time: {time_6hr}\n Temperature: {temp_6hr}\n Feels like: {feels_6hr}\n The weather is {weather_desc_6hr}\n\n\n Time: {time_9hr}\n Temperature: {temp_9hr}\n Feels like: {feels_9hr}\n The weather is {weather_desc_9hr}\n ------------------------\n\n Place: {place_1}\n Time: {time_6hr_1}\n Temperature: {temp_6hr_1}\n Feels like: {feels_6hr_1}\n The weather is {weather_desc_6hr_1}\n\n\n Time: {time_9hr_1}\n Temperature: {temp_9hr_1}\n Feels like: {feels_9hr_1}\n The weather is {weather_desc_9hr_1}. \n\nThere is no forcast of rain today. You may leave your ☂️ at home'


if weather_6hr == 'Rain' or weather_9hr == 'Rain' or weather_6hr_1 == 'Rain' or weather_9hr_1 == 'Rain':
    message = client.messages \
                .create(
                     body= message_rain,
                     from_='+16204009986',
                     to= '+447360059436'
                 )

    print(message.status)
else:
    message = client.messages \
                .create(
                     body= message,
                     from_='+16204009986',
                     to= '+447360059436'
                 )

    print(message.status)

    

