import streamlit as st
import folium
from streamlit_folium import folium_static
import os
import json

from Algoritimos import BuscaLargura, BuscaProfundidade, AEstrela

# Adicionando Título na guia da Página 
st.set_page_config(page_title="Trabalho - Inteligência Artificial", page_icon="🌍")

# Adicionando Título a nossa Aplicação
st.title("Viagem de Trem pela Europa.")

# Carregar o arquivo CSS
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Lista de coordenadas das capitais da Europa
caminho_arquivo_detalhes = os.path.join(os.path.dirname(__file__), '..', 'APIs', 'city_details.json')
with open(caminho_arquivo_detalhes, 'r', encoding='utf-8') as arquivo:
    cidades_detalhes = json.load(arquivo)


coordenadas = {}
for cidade, detalhes in cidades_detalhes.items():
    coordenadas[cidade] = [detalhes['latitude'], detalhes['longitude']]


# Selecionar o país de origem
country_from = st.selectbox("Selecione a capital de origem:", list(coordenadas.keys()))

# Selecionar o país de destino
country_to = st.selectbox("Selecione a capital de destino:", list(coordenadas.keys()))

# Validação para evitar seleção igual
if country_from == country_to:
    st.warning("Por favor, selecione capitais diferentes para origem e destino.")

# Selecionar o algoritmo
algorithm = st.selectbox("Escolha o algoritmo:", ["Busca em Largura", "Busca em Aprofundamento Interativo", "A*"])

# Criação de um espaço vazio para o mapa
map_placeholder = st.empty()

# Botão para executar a busca
if st.button("Buscar Rota"):
    if country_from != country_to:
        # Criação do mapa
        map_center = [50.8503, 4.3517]  # Coordenadas aproximadas do centro da Europa
        m = folium.Map(location=map_center, zoom_start=4)

        # Adicionando marcadores das cidades
        folium.Marker(coordenadas[country_from], popup=country_from).add_to(m)
        folium.Marker(coordenadas[country_to], popup=country_to).add_to(m)

        # Exibir o mapa no Streamlit
        folium_static(m, width=700, height=500)

        # Apresentar informações da busca
        st.write(f"Buscando rota de {country_from} para {country_to} usando o algoritmo {algorithm}...")
        # Simulação de resultados
        st.write("Rota: ...")
        st.write("Distância total: ...")
        st.write("Nós gerados: ...")
        st.write("Nós expandidos: ...")
        st.write("Tempo de execução: ...")

# Adicionando um rodapé
st.markdown("""<footer style='text-align: center; margin-top: 50px;'>
    <hr>
    <p>Trabalho de Inteligência Artificial - Viagem de Trem pela Europa.</p>
    <p>Desenvolvido por Anthoni, Elias, Gustavo, Nickael e Paulo</p>
    <p><a href="https://github.com/EliasViniciusRaitz/ViagemTremEuropa" target="_blank">Acesse o repositório do GitHub!</a></p>
</footer>""", unsafe_allow_html=True)
