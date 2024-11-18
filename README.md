# Viagem de Trem pela Europa 🌍🚂

**Trabalho de Inteligência Artificial** - Simulação de viagem de trem entre capitais da Europa utilizando diferentes algoritmos de busca.

---

## Tecnologias Utilizadas

- **Streamlit**: Para criação da interface web interativa.
- **Folium**: Para renderização de mapas interativos.
- **Streamlit-Folium**: Para integrar o Folium ao Streamlit.

## Instale as Dependências

pip install streamlit
pip install folium
pip install streamlit-folium

## Inicie o Sistema

streamlit run main.py ou python -m streamlit run main.py

---

Algoritmo de Busca Clássica. Consiste na implementação dos seguintes algoritmos: Largura, Aprofundamento Interativo e A* encontrando o caminho para uma viagem de trem entre dois países da Europa.

### Ambiente virtual do Python

Se não instalado o virtualenv.
No terminal: ``pip install virtualenv``

Para inicializar o ambiente virtual:

1. Navegar até a pasta anterior à do projeto
2. Executar o seguinte comando:
   * Linux e MacOS: ``source /bin/activate``
   * Windows: ``./bin/activate``
     Aparecerá (ViagemTremEuropa) no terminal.
3. Então, realizar a instalação das bibliotecas necessárias através do
   ``pip install biblioteca_dejejada``

### Uso da API Google

 Incluir na pasta raiz do projeto um arquivo JSON com o nome ``google_api_key.json``
 Seguinte formato:

```
{
    "key": "SUA_API_GOOGLE_AQUI"
}
```
