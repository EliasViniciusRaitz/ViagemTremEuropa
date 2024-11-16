import streamlit as st
import folium
from streamlit_folium import folium_static

# Adicionando Título na guia da Página 
st.set_page_config(page_title="Trabalho - Inteligência Artificial", page_icon="🌍")

# Adicionando Título a nossa Aplicação
st.title("Viagem de Trem pela Europa.")

# Carregar o arquivo CSS
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Lista de coordenadas das capitais da Europa
coordenadas = {
    "Amsterdã": [52.3676, 4.9041],
    "Andorra-a-Velha": [42.5063, 1.5211],
    "Atenas": [37.9838, 23.7275],
    "Belgrado": [44.7866, 20.4489],
    "Berlim": [52.5200, 13.4050],
    "Bratislava": [48.1482, 17.1067],
    "Bruxelas": [50.8503, 4.3517],
    "Bucareste": [44.4268, 26.1025],
    "Budapeste": [47.4979, 19.0402],
    "Copenhague": [55.6761, 12.5683],
    "Dublin": [53.3498, -6.2603],
    "Estocolmo": [59.3293, 18.0686],
    "Helsinque": [60.1695, 24.9354],
    "Kiev": [50.4501, 30.5234],
    "Lisboa": [38.7223, -9.1393],
    "Liubliana": [46.0569, 14.5051],
    "Londres": [51.5074, -0.1278],
    "Luxemburgo": [49.6118, 6.1319],
    "Madri": [40.4168, -3.7038],
    "Minsk": [53.9045, 27.5590],
    "Moscou": [55.7558, 37.6173],
    "Oslo": [59.9139, 10.7522],
    "Paris": [48.8566, 2.3522],
    "Podgorica": [42.4411, 19.2636],
    "Praga": [50.0755, 14.4378],
    "Reiquiavique": [64.1355, -21.8954],
    "Riga": [56.9496, 24.1052],
    "Roma": [41.9028, 12.4964],
    "San Marino": [43.9333, 12.4462],
    "Sarajevo": [43.8486, 18.3564],
    "Skopje": [41.9973, 21.4280],
    "Sofia": [42.6977, 23.3219],
    "Tallinn": [59.4372, 24.7536],
    "Tbilisi": [41.7151, 44.8271],
    "Tirana": [41.3275, 19.8189],
    "Vaduz": [47.1415, 9.5215],
    "Valeta": [35.8989, 14.5149],
    "Varsóvia": [52.2297, 21.0122],
    "Vaticano": [41.9029, 12.4534],
    "Viena": [48.2082, 16.3738],
    "Vilnius": [54.6872, 25.2797],
    "Zagreb": [45.8150, 15.9819]
}

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
