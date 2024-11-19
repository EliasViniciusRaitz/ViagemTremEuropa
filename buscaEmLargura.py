from queue import Queue
import json
import os

class Estado:
    def __init__(self, cidade, pai):
        self.cidade = cidade
        self.pai = pai

class Tree:
    def __init__(self):
        self.nodes = {}

    def create_node(self, cidade, estado, parent=None):
        self.nodes[cidade] = estado

    def show(self):
        for cidade, estado in self.nodes.items():
            if estado.pai:
                print(f"{estado.cidade} (pai: {estado.pai.cidade})")
            else:
                print(f"{estado.cidade} (pai: None)")

class Busca:
    def __init__(self):
        caminho_arquivo = os.path.join(os.path.dirname(__file__), 'Grafos', 'origins_destinations.json')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            self.rotas = json.load(arquivo)

    def busca(self, origem, destino, fronteira):
        atual = Estado(origem, None)
        fronteira.put(atual)
        visitados = set()
        visitados.add(atual.cidade)
        qtdVisitados = 1
        qtdExpandidos = 0
        arvore = Tree()
        arvore.create_node(atual.cidade, atual)
        resultado = None

        while not fronteira.empty() and resultado is None:
            atual = fronteira.get()
            qtdExpandidos += 1
            resultado, fronteira, visitados, qtdVisitados, arvore = self.geraFilhos(atual, destino, fronteira, visitados, qtdVisitados, arvore)

        return resultado, qtdVisitados, qtdExpandidos, arvore

    def geraFilhos(self, atual, destino, fronteira, visitados, qtdVisitados, arvore):
        cidades = self.rotas.get(atual.cidade, [])
        for c in cidades:
            if c == destino:
                qtdVisitados += 1
                novo = Estado(c, atual)
                visitados.add(c)
                arvore.create_node(c, novo, parent=atual)
                return novo, fronteira, visitados, qtdVisitados, arvore
            elif atual.pai is None or c != atual.pai.cidade:
                qtdVisitados += 1
                novo = Estado(c, atual)
                fronteira.put(novo)
                visitados.add(c)
                arvore.create_node(c, novo, parent=atual)

        return None, fronteira, visitados, qtdVisitados, arvore

    def mostraResultado(self, resultado, qtdVisitados, qtdExpandidos, arvore):
        if resultado is None:
            print('Solução não encontrada.')
        else:
            print('*** Rota encontrada ***')
            caminho = []
            while resultado is not None:
                caminho.append(resultado.cidade)
                resultado = resultado.pai

            print(' -> '.join(reversed(caminho)))

        print('Estados visitados:', qtdVisitados)
        print('Estados expandidos:', qtdExpandidos)
        print('**** Árvore gerada ****')
        arvore.show()

class BuscaLargura(Busca):
    def __init__(self):
        super().__init__()

    def realizaBusca(self, origem, destino):
        fronteira = Queue()
        resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, fronteira)
        self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)
        return resultado, qtdVisitados, qtdExpandidos

# Exemplo de execução
if __name__ == "__main__":
    origins = input("Digite a cidade de origem: ")
    destinations = input("Digite a cidade de destino: ")

    algbusca = BuscaLargura()
    rota = algbusca.realizaBusca(origins, destinations)
