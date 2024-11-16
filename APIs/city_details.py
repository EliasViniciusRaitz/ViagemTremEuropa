import requests
import os
import json


def carrega_api_key_google():
    caminho_chave_api = os.path.join(os.path.dirname(__file__), '..', 'google_api_key.json')
    with open(caminho_chave_api, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)['key']

def carrega_json_origins_destinations():
    try:
        caminho_arquivo = os.path.join(os.path.dirname(__file__),'..', 'Grafos', 'origins_destinations.json')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None

# Defina a URL da API e sua chave de API
url = "https://places.googleapis.com/v1/places:searchText"
api_key = carrega_api_key_google()

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": api_key,
    "X-Goog-FieldMask": "*"
    # places.displayName.text,places.formattedAddress,places.location.latitude,places.location.longitude"
}
try:
    caminho_resposta_api = os.path.join(os.path.dirname(__file__),'..', 'APIs', 'city_details.json')
    with open(caminho_resposta_api, "r", encoding='utf-8') as file:
        content = file.read()
        if content == "":
            resposta = {}
        else:
            resposta = json.loads(content)
except FileNotFoundError:
    resposta = {}

for cidade, destinos in carrega_json_origins_destinations().items():
    

    # Dados da consulta
    data = {
        "textQuery": cidade,
        "languageCode": "pt-BR",
        "locationBias": {
            "rectangle": {
                "low": {
                    "latitude": 35.0,
                    "longitude": -10.0
                },
                "high": {
                    "latitude": 70.0,
                    "longitude": 40.0
                }
            } 
        }
    }

    
    # Envia a requisição POST
    response = requests.post(url, json=data, headers=headers)


    # # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Carrega a resposta da API
        nomeCidade= response.json()['places'][0]['displayName']['text']
        paisCidade = response.json()['places'][0]['formattedAddress']
        for i in range(len(response.json()['places'][0]['addressComponents'])):
            tipo = response.json()['places'][0]['addressComponents'][i]['types'][0]
            if tipo == "country":
                pais = response.json()['places'][0]['addressComponents'][i]['longText']
        # pais = response.json()['places'][0]['addressComponents'][-1]['longText']
        # if response.json()['places'][0]['addressComponents'][-1]['types'] == "postal_code":
        #     pais = response.json()['places'][0]['addressComponents'][-2]['longText']
        if pais == "Reino Unido":
            pais = response.json()['places'][0]['addressComponents'][-2]['longText']
        latitude = response.json()['places'][0]['location']['latitude']
        longitude = response.json()['places'][0]['location']['longitude']

        resposta_atual = {
            "paisCidade": paisCidade,
            "pais": pais,
            "latitude": latitude,
            "longitude": longitude
            }
        
        resposta[nomeCidade] = resposta_atual

    else:
        # Imprime o código de status em caso de erro
        print(f"Erro: {response.status_code}")
        print(response.text)
    # else:
    #     # Imprime o código de status em caso de erro
    #     print(f"Erro: {response.status_code}")
    #     print(response.text)



with open(caminho_resposta_api, "w", encoding='utf-8') as file:
    json.dump(resposta, file, ensure_ascii=False, indent=4)