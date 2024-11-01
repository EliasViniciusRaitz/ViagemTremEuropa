import json
from busca_distancias_api_google import carrega_json_da_api_google

def carrega_json_origins_destinations():
    try:
        with open('./ViagemTremEuropa/Grafos/origins_destinations.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None

def carrega_distancias():
    try:
        with open('./ViagemTremEuropa/Grafos/distancias.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

json_origins_destinations = carrega_json_origins_destinations()
distancias = carrega_distancias()

if json_origins_destinations is not None:
    for origin, destinations in json_origins_destinations.items():
        jsonResposta = carrega_json_da_api_google(origin, destinations)
        distancias.update(jsonResposta)
        
    with open('./ViagemTremEuropa/Grafos/distancias.json', 'w', encoding='utf-8') as arquivo:
        json.dump(distancias, arquivo, indent=4)
else:
    print("Erro ao carregar arquivo json")