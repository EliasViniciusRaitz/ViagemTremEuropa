import os
import json
import requests


def carrega_json_da_api_google(origins, destinations):
    url_api_google = f"https://maps.googleapis.com/maps/api/distancematrix/json"
    api_key = carrega_api_key_google()
    response = requests.get(url_api_google, params={'origins': origins, 'destinations': destinations, 'key': api_key})
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# Caminho relativo ao arquivo google_api_key.json
def carrega_api_key_google():
    caminho_chave_api = os.path.join(os.path.dirname(__file__), '..', 'google_api_key.json')
    with open(caminho_chave_api, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)['key']

if __name__ == '__main__':
    origins = input("Digite a cidade de origem: ")
    destinations = input("Digite a cidade de destino: ")

    jsonResposta = carrega_json_da_api_google(origins, destinations)

    distance = jsonResposta['rows'][0]['elements'][0]['distance']['text']

    print("Distânca entre as cidades é: ", distance)