from busca_distancias_api_google import carrega_json_da_api_google
import json
import os

def carrega_json_origins_destinations():
    try:
        caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'Grafos', 'origins_destinations.json')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None

json_origins_destinations = carrega_json_origins_destinations()
cities = []
if json_origins_destinations is not None:
    for origin in json_origins_destinations.items():
        cities.append(origin[0])

for origin in cities:
    for destination in cities:
        if origin != destination:
            jsonResposta = carrega_json_da_api_google(origin, destination)
            distancia_value = jsonResposta.get('rows', [])[0].get('elements', [])[0].get('distance', {}).get('value', None)
            if origin in json_origins_destinations:
                json_origins_destinations[origin].append((destination, distancia_value))
            else:
                json_origins_destinations[origin] = [(destination, distancia_value)]
    
caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'Grafos', 'distancies_heuristicas.json')
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(json_origins_destinations, arquivo, ensure_ascii=False, indent=4)