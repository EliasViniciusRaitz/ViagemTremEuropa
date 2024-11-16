from treelib import Node, Tree
import os
from queue import LifoQueue
import json

class Pais:
  def __init__(self, pais, pai, nivel):
    self.pais = pais
    self.pai = pai
    self.nivel = nivel



class BuscaProfundidadeLimitada:

    def __init__(self):
        caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'Grafos', 'origins_destinations.json')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            self.rotas = json.load(arquivo)


    def realizaBusca(self, origem, destino, limite):
        fronteira = LifoQueue()
        resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, limite, fronteira)
        self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)

    def busca(self, origem, destino, limite, fronteira):
        atual = Pais(origem, None, 0)
        fronteira.put(atual)
        visitados = set()
        visitados.add(atual.pais)  
        qtdVisitados = 1
        qtdExpandidos = 0
        arvore = Tree()
        arvore.create_node(atual.pais, atual)  
        resultado = None

        while not fronteira.empty() and resultado is None:
            atual = fronteira.get()
            qtdExpandidos += 1
            resultado, fronteira, visitados, qtdVisitados, arvore = self.geraFilhos(atual, destino, fronteira, visitados, qtdVisitados, arvore, limite)
        return resultado, qtdVisitados, qtdExpandidos, arvore

    def geraFilhos(self, atual, destino, fronteira, visitados, qtdVisitados, arvore, limite):
        paises_vizinhos = self.rotas.get(atual.pais, [])
        for pais in paises_vizinhos:
            if pais == destino:
                qtdVisitados += 1
                novo = Pais(pais, atual, atual.nivel + 1)
                visitados.add(pais)
                arvore.create_node(pais, novo, parent=atual)
                return novo, fronteira, visitados, qtdVisitados, arvore
            elif pais not in visitados:
                qtdVisitados += 1
                visitados.add(pais)
                novo = Pais(pais, atual, atual.nivel + 1)
                arvore.create_node(pais, novo, parent=atual)
                if atual.nivel + 1 < limite:
                    fronteira.put(novo)
        return None, fronteira, visitados, qtdVisitados, arvore

    def mostraResultado(self, resultado, qtdVisitados, qtdExpandidos, arvore):
        if resultado is None:
            print('Solução não encontrada.')
        else:
            print('***Rota encontrada***')
            while resultado is not None:
                print(resultado.pais)
                resultado = resultado.pai
        print('Cidades visitados: ', qtdVisitados)
        print('Cidades expandidos: ', qtdExpandidos)
        print('****Árvore gerada****')

        # Mostrar a árvore corretamente como string
        arvore.show()

class BuscaAprofundamentoIterativo(BuscaProfundidadeLimitada):

    def __init__(self):
        super().__init__()

    def realizaBusca(self, origem, destino):
        for i in range(1, 10):
            fronteira = LifoQueue()
            print("****limite ", i, " ***")
        return self.busca(origem, destino, i, fronteira)


if __name__ == '__main__':
    origins = input("Digite a cidade de origem: ")
    destinations = input("Digite a cidade de destino: ")

    algbusca = BuscaAprofundamentoIterativo()
    resultado, qtdVisitados, qtdExpandidos, arvore = algbusca.realizaBusca(origins,destinations)

    if resultado is not None:
        algbusca.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)