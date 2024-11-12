import json
from busca_distancias_api_google import carrega_json_da_api_google
import os

def carrega_json_origins_destinations():
    try:
        caminho_arquivo = os.path.join('..', 'Grafos', 'origins_destinations.json')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None


json_origins_destinations = carrega_json_origins_destinations()

if json_origins_destinations is not None:
    for origin, destinations in json_origins_destinations.items():
        for destination in destinations:
            destination_index = destinations.index(destination)
            if destination is not None:
                jsonResposta = carrega_json_da_api_google(origin, destination)
                distancia_value = jsonResposta.get('rows', [])[0].get('elements', [])[0].get('distance', {}).get('value', None)
                if distancia_value is not None:
                    json_origins_destinations[origin][destination_index] = (destination, distancia_value)
    caminho_arquivo = os.path.join('..', 'Grafos', 'origins_destinations_distancies.json')
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(json_origins_destinations, arquivo, ensure_ascii=False, indent=4)
else:
    print("Erro ao carregar arquivo json")