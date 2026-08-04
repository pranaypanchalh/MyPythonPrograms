import requests

parameters = {
    "lat" : 51.507351,
    "lng" : -0.127758
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

print(data)