#https://hackmd.io/@lukac/apiOM
"""
avto={"znamka":"nissan", "model":"GT-R R35","Letnik":"2022" }
print(avto.items())

for avto["znamka"] in avto.items():
    print(avto["znamka"])



"""
# ------------------------------------------------


"""
sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}

print(sola["naslov"]["kraj"])   # Kranj
print(sola["smeri"][0])         # računalništvo
print(len(sola["smeri"]))       # 3

print(sola["naslov"]["posta"],sola["smeri"][len(sola["smeri"])-1])

"""
#---------------------------------------------------------

"""
import requests

url = "https://api.open-meteo.com/v1/forecast"
parametri = {
    "latitude": 500,
    "longitude": 14.5058,
    "current": "temperature_2m,wind_speed_10m"
}

odgovor = requests.get(url, params=parametri)

print(odgovor.status_code)   # 200 pomeni, da je vse v redu
podatki = odgovor.json()     # JSON pretvorimo v slovar
print(podatki)

# če daš nad 500 javi da je izven intervala

"""

#-------------------------------------------------------------

"""
import requests

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast?latitude=46.0569,46.5547,46.252130243655834&longitude=14.5058,15.6459,14.348579694327805&current=temperature_2m&forecast_days=1"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


kraji = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
    "Kranj":(46.2521, 14.3486)
}

for ime, (lat, lon) in kraji.items():
    t = trenutna_temperatura(lat, lon)
    print(f"{ime}: {t} °C")

"""

# ------------------------------------------

"""
temperature = {
    "Ljubljana": 14.2,
    "Maribor": 15.1,
    "Koper": 18.4,
    "Kamnik": 12.9,
    "Piran" : 9.2,
    "Kamnik": 23.3
}

najhladnejše = "Ljubljana"
najnižja = temperature["Ljubljana"]

for mesto, t in temperature.items():
    if t < najnižja:
        najnižja = t
        najhladnejše = mesto

print(f"Najtoplejše: {najhladnejše} ({najnižja} °C)")


"""
# ----------------------------------------------


mesta = {
    "Ljubljana":  (46.0569, 14.5058),
    "Maribor":    (46.5547, 15.6459),
    "Kranj":      (46.2389, 14.3556),
    "Celje":      (46.2361, 15.2675),
    "Koper":      (45.5481, 13.7302),
    "Velenje":    (46.3592, 15.1103),
    "Novo mesto": (45.8040, 15.1689),
    "Ptuj":       (46.4200, 15.8700),
    "Trbovlje":   (46.1550, 15.0533),
    "Kamnik":     (46.2259, 14.6121),
}

import requests

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast?latitude=45&longitude=13.41&current=temperature_2m&forecast_days=1"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


for ime, (lat, lon) in mesta.items():
    t = trenutna_temperatura(lat, lon)
    print(f"{ime}: {t} °C")