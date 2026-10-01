import requests
url="https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"
klic = requests.get(url)
klicjason=klic.json()
print(klicjason["current"]["temperature_2m"])