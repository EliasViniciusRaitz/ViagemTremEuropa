from treelib import Node, Tree
import os
from queue import LifoQueue
import json

class Estado:
  def __init__(self, pais, pai, gn, hn):
    self.pais = pais
    self.pai = pai
    self.gn = gn
    self.fn = gn + hn

class BuscaHeuristica:

      def __init__(self):
            try:
                  caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'Grafos', 'origem_destino_distancies.json')
                  with open(caminho_arquivo, 'r') as arquivo:
                        self.rotas = json.load(arquivo)
            except:
                  print("Erro ao carregar arquivo de rotas")
                  self.rotas = {}

            self.heuristicas

      def realizaBusca(self, origem, destino):
            fronteira = []
            resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, fronteira)
            self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)

      def busca(self, origem, destino, fronteira):
            distancias = self.heuristicas.get(origem, [])
            for d in distancias:
                  if d[0]==destino:
                        hn = d[1]
            atual = Estado(origem, None, 0, hn)
            fronteira.append(atual)
            visitados = set()
            visitados.add(atual.pais)
            qtdVisitados = 1
            qtdExpandidos = 0
            arvore = Tree()
            arvore.create_node(atual.pais+' - '+str(hn), atual)

            resultado = None
            while len(fronteira)!=0:
                  fronteira.sort(key=lambda x: x.fn)
                  atual = fronteira.pop(0)
                  if atual.pais == destino:
                        resultado = atual
                  break
                  qtdExpandidos += 1
                  fronteira, qtdVisitados, arvore = self.geraFilhos(atual, destino, fronteira, qtdVisitados, arvore)

            return resultado, qtdVisitados, qtdExpandidos, arvore

      def ehAncestral(self, pais, nodo):
            while nodo != None:
                  if pais == nodo.pais:
                        return True
                  nodo = nodo.pai
            return False

      def geraFilhos(self, atual,  destino, fronteira, qtdVisitados, arvore):
            paises = self.rotas.get(atual.pais)
            for c in paises:

                  if atual.pai == None or not self.ehAncestral(c[0],atual.pai):
                        qtdVisitados += 1
                  distancias = self.heuristicas.get(c[0])
                  for d in distancias:
                        if d[0]==destino:
                              hn = d[1]

                  novo = Estado(c[0], atual, atual.gn + c[1], hn)
                  fronteira.append(novo)

                  arvore.create_node(c[0]+' - '+str(hn), novo, parent=atual)

            return fronteira, qtdVisitados, arvore

      def mostraResultado(self, resultado, qtdVisitados, qtdExpandidos, arvore):
            if (resultado==None):
                  print('Solução não encontrada.')
            else:
                  print('***Rota encontrada***')
                  print('A distância total da viagem é', resultado.gn,'Km')
                  print('---ROTA---')
                  while (resultado != None):
                        print(resultado.pais,'-',resultado.gn)
                  resultado = resultado.pai
            print('----------')
            print('Estados visitados: ',qtdVisitados)
            print('Estados expandidos: ',qtdExpandidos)
            print('****Árvore gerada****')
            arvore.show()

if __name__ == '__main__':
      algbusca = BuscaHeuristica()
      algbusca.realizaBusca('Lisboa','Berlim')