# import requests

# url = "https://obserwatoriumbrd.pl/app/api/nodes/post_zdarzenia.php"

# payload = {'type': 'DETAILS',
# 'rok[]': '2023',
# 'rok[]': '2022',
# 'wybrane_wojewodztwa[]': '12',
# 'rodzaj_pojazdu_ofiary[]': '10',
# 'obszar_mapy[topRightCorner][lat]': '51.014104478487866',
# 'obszar_mapy[topRightCorner][lng]': '23.299255371093754',
# 'obszar_mapy[bottomLeftCorner][lat]': '48.81761408933224',
# 'obszar_mapy[bottomLeftCorner][lng]': '16.064758300781254'}
# files=[]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    events = []
    
    for wojewodztwo in data["mapa"]["wojewodztwa"]:
        woj_nazwa = wojewodztwo["woj_nazwa"]
        for powiat in wojewodztwo["powiaty"]:
            pow_nazwa = powiat["pow_nazwa"]
            for gmina in powiat["gminy"]:
                gmi_nazwa = gmina["gmi_nazwa"]
                mie_nazwa = gmina["mie_nazwa"]
                for zdarzenie in gmina["zdarzenia_detale"]:
                    events.append([
                        zdarzenie["id"],
                        zdarzenie["wsp_gps_x"],
                        zdarzenie["wsp_gps_y"],
                        zdarzenie["ciezkosc"],
                        mie_nazwa.strip(),
                        gmi_nazwa,
                        pow_nazwa,
                        woj_nazwa
                    ])
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "wsp_gps_x", "wsp_gps_y", "ciezkosc", "mie_nazwa", "gmi_nazwa", "pow_nazwa", "woj_nazwa"])
        writer.writerows(events)

# Użycie funkcji
json_file = 'D:\\DEV\\GIT\\HackYeah2024\\accidents\\zdarzenia_all.json'  # Podaj ścieżkę do pliku wejściowego JSON
csv_file = 'D:\\DEV\\GIT\\HackYeah2024\\accidents\\output.csv'           # Podaj ścieżkę do pliku wyjściowego CSV

json_to_csv(json_file, csv_file)