import streamlit as st
import folium
from streamlit_folium import folium_static
import os
import json

from buscaProfundidadeInterativa import BuscaAprofundamentoIterativo
from buscaEmLargura import BuscaLargura
# from buscaAEstrela import BuscaHeuristica as bae

# Adicionando Título na guia da Página 
st.set_page_config(page_title="Trabalho - Inteligência Artificial", page_icon="🌍")

# Adicionando Título a nossa Aplicação
st.title("Viagem de Trem pela Europa.")

# Carregar o arquivo CSS
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Lista de coordenadas das capitais da Europa
caminho_arquivo_detalhes = os.path.join(os.path.dirname(__file__), 'APIs', 'city_details.json')
with open(caminho_arquivo_detalhes, 'r', encoding='utf-8') as arquivo:
    cidades_detalhes = json.load(arquivo)


coordenadas = {}
for cidade, detalhes in cidades_detalhes.items():
    coordenadas[cidade.strip()] = [detalhes['latitude'], detalhes['longitude']]


# Selecionar o país de origem
country_from = st.selectbox("Selecione a capital de origem:", list(coordenadas.keys()))
country_from = country_from.strip()

# Selecionar o país de destino
country_to = st.selectbox("Selecione a capital de destino:", list(coordenadas.keys()))
country_to = country_to.strip()

# Validação para evitar seleção igual
if country_from == country_to:
    st.warning("Por favor, selecione capitais diferentes para origem e destino.")

# Selecionar o algoritmo
algorithm = st.selectbox("Escolha o algoritmo:", ["Busca em Largura", "Busca em Aprofundamento Interativo", "Busca Heurística (A*)"])

# Criação de um espaço vazio para o mapa
map_placeholder = st.empty()

# Botão para executar a busca
if st.button("Buscar Rota"):

    if algorithm == "Busca em Largura":
        algoritmoBusca = BuscaLargura()
        roteiro, qtdVisitados, qtdExpandidos = algoritmoBusca.realizaBusca(country_from, country_to)
        caminho = []
        while roteiro is not None:
            caminho.append(roteiro.cidade)
            roteiro = roteiro.pai

    elif algorithm == "Busca em Aprofundamento Interativo":
        algoritmoBusca = BuscaAprofundamentoIterativo()
        roteiro, qtdVisitados, qtdExpandidos = algoritmoBusca.realizaBusca(country_from, country_to)
        caminho = []
        while roteiro is not None:
            caminho.append(roteiro.pais)
            roteiro = roteiro.pai

    # elif algorithm == "Busca Heurística (A*)":
    #     algoritmoBusca = bae
    else:
        st.error("Algoritmo não reconhecido.")

    

    if country_from != country_to:
        # Criação do mapa
        map_center = [50.8503, 4.3517]  # Coordenadas aproximadas do centro da Europa
        m = folium.Map(location=map_center, zoom_start=4)

        # Adicionando marcadores das cidades
        for i in range(len(caminho) - 1):
            cidade_origem = caminho[i]
            cidade_destino = caminho[i + 1]
            folium.PolyLine([coordenadas[cidade_origem], coordenadas[cidade_destino]], color="red", weight=2.5, opacity=1).add_to(m)
            folium.Marker(coordenadas[cidade_origem], popup=cidade_origem).add_to(m)
        folium.Marker(coordenadas[cidade_destino], popup=cidade_destino).add_to(m)

        # Exibir o mapa no Streamlit
        folium_static(m, width=700, height=500)

        # Apresentar informações da busca
        st.write(f"Buscando rota de {country_from} para {country_to} usando o algoritmo {algorithm}...")
        # Simulação de resultados
        st.write("Rota: ", caminho[::-1])
        # st.write("Distância total: ...")
        st.write("Nós visitados: ", qtdVisitados)
        st.write("Nós expandidos: ", qtdExpandidos)
        # st.write("Tempo de execução: ...")

# Adicionando um rodapé
st.markdown("""<footer style='text-align: center; margin-top: 50px;'>
    <hr>
    <p>Trabalho de Inteligência Artificial - Viagem de Trem pela Europa.</p>
    <p>Desenvolvido por Anthoni, Elias, Gustavo, Nickael e Paulo</p>
    <p><a href="https://github.com/EliasViniciusRaitz/ViagemTremEuropa" target="_blank">Acesse o repositório do GitHub!</a></p>
</footer>""", unsafe_allow_html=True)
