"""
import requests

url = "https://api.frankfurter.dev/v1/latest"
parametri = {
    "base": "EUR",          # iz katere valute
    "symbols": "USD,GBP"    # v katere valute
}

odgovor = requests.get(url, params=parametri)

print(odgovor.url)


print(odgovor.json())

"""
"""
import requests

url = "https://api.frankfurter.dev/v1/latest"
odgovor = requests.get(url, params={"symbols": "USD,GBP,CHF,JPY"})

# brez uspešnega odgovora nima smisla nadaljevati
if odgovor.status_code != 200:
    print("Napaka.")
    exit()

podatki = odgovor.json()
tecaji = podatki["rates"]   # slovar valuta -> tečaj

print("Tečaji na dan", podatki["date"])

for valuta, tecaj in tecaji.items():
    print(valuta + ":", tecaj)

print("Skupaj valut:", len(tecaji))
"""
"""
import requests

url = "https://api.frankfurter.dev/v1/latest"
podatki=requests.get(url).json()
tecaji=podatki["rates"]

def pretvorba_v_tujo(denar,valuta,tecaji):
    if valuta not in tecaji:
        return None
    return denar*tecaji[valuta]

def pretvorba_v_evre(znesek,valuta,tecaji):
    if valuta not in tecaji:
        return None
    return znesek/tecaji[valuta]


denar=float(input("Vnesi znesek: "))
valuta=str(input("Vnesi vneseno valuto: ")).upper()
tuje=pretvorba_v_tujo(denar,valuta,tecaji)

if tuje is None:
    print(f"Valuta {valuta} ne obstaja")
else:
    print(f"{denar} EUR {round(tuje,2)} {valuta}")
    nazaj = pretvorba_v_evre(tuje,valuta,tecaji)
    print(f"{round(tuje,2)} {valuta} = {round(nazaj,2)} EUR")
"""
#-------------------------------------------------------------

"""
import requests
url="https://api.frankfurter.dev/v1/2026-09-01..2026-09-07"
podatki=requests.get(url,params={"symbols":"USD"}).json()
dnevi=podatki["rates"]

datumi = list(dnevi.keys()) 
print(datumi[0]+":",dnevi[datumi[0]]["USD"])

for i in range(1,len(datumi)):
    danes=dnevi[datumi[i]]["USD"]
    vceraj=dnevi[datumi[i-1]]["USD"]
    
    if danes>vceraj:
        smer="gor"
    elif vceraj>danes:
        smer="dol"
    else:
        smer="enako"

    print(datumi[i]+":", danes,"("+ smer +")")

print("podatki od ", datumi[0],"do",datumi[-1], "in skupaj", len(datumi), "dni")
"""
#------------------------------------------------------------------------
"""
import requests

valute = ["USD", "GBP", "CHF"]

url = "https://api.frankfurter.dev/v1/latest"
podatki = requests.get(url, params={"symbols": ",".join(valute)}).json()
tecaji = podatki["rates"]


for a in valute:
    for b in valute:
        if a==b:
            continue
tecaj=tecaji[b]/tecaji[a]
print("1",a,"=" , round(tecaj,4),b)
"""

import requests
url="https://api.frankfurter.dev/v1/2026-09-01..2026-09-30"
podatki=requests.get(url,params={"symbols":"GBP"}).json
dnevi=podatki["rates"]

prihranki=800


prvi_dan=list(dnevi.keys())[0]
najboljši=prvi_dan
najslabši=prvi_dan


for datum, tecaji_dne in dnevi.items():
    tecaj=tecaji_dne()

    if tecaj > dnevi[najboljši]["GBP"]:
        najboljši=datum
    elif tecaj <dnevi[najslabši]["GBP"]:
        najslabši=datum

vsota=vsota+tecaj