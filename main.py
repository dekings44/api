import requests


# response = requests.get(url = 'http://api.open-notify.org/iss-now.json')

# data = response.json()

# lat = data['iss_position']['latitude']
# lng = data['iss_position']['longitude']

# coord = (lat,lng)

# print(coord)

response = requests.get(url = 'http://api.sunrise-sunset.org/json')

print(response.json())