import requests
from datetime import datetime


# response = requests.get(url = 'http://api.open-notify.org/iss-now.json')

# data = response.json()

# lat = data['iss_position']['latitude']
# lng = data['iss_position']['longitude']

# coord = (lat,lng)

# print(coord)

time_now = datetime.now()

my_lat = 54.760731
my_lng = -1.332580

parameter = {
    'lat' : my_lat,
    'lng' : my_lng,
    'formatted': 0
}

response = requests.get('http://api.sunrise-sunset.org/json', params=parameter)

response

data = response.json()
sun_rise = data['results']['sunrise'].split('T')[1].split(':')[0]
sun_set = data['results']['sunset'].split('T')[1].split(':')[0]

print(f'The current hour is {time_now.hour}, the sun will rise at {sun_rise} and set at {sun_set}')
