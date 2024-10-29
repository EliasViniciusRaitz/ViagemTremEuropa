from treelib import Node, Tree

class Pais:
  def __init__(self, pais, pai, nivel):
    self.pais = pais
    self.pai = pai
    self.nivel = nivel

from queue import LifoQueue

class BuscaProfundidadeLimitada:

    def __init__(self):
        self.rotas = {
            'Albânia': ['Grécia', 'Macedônia do Norte', 'Kosovo', 'Montenegro'],
            'Alemanha': ['Dinamarca', 'Polônia', 'República Tcheca', 'Áustria', 'Suíça', 'França', 'Luxemburgo', 'Bélgica', 'Países Baixos'],
            'Andorra': ['França', 'Espanha'],
            'Áustria': ['Alemanha', 'República Tcheca', 'Eslováquia', 'Hungria', 'Eslovênia', 'Itália', 'Suíça', 'Liechtenstein'],
            'Belarus': ['Letônia', 'Lituânia', 'Polônia', 'Ucrânia'],
            'Bélgica': ['França', 'Alemanha', 'Luxemburgo', 'Países Baixos'],
            'Bósnia e Herzegovina': ['Croácia', 'Montenegro', 'Sérvia'],
            'Bulgária': ['Grécia', 'Macedônia do Norte', 'Romênia', 'Sérvia'],
            'Croácia': ['Bósnia e Herzegovina', 'Hungria', 'Montenegro', 'Sérvia', 'Eslovênia'],
            'Chipre': [],
            'Dinamarca': ['Alemanha'],
            'Escócia': ['Irlanda'], ## REINO UNIDO
            'Eslováquia': ['Áustria', 'República Tcheca', 'Hungria', 'Polônia', 'Ucrânia'],
            'Eslovênia': ['Áustria', 'Croácia', 'Hungria', 'Itália'],
            'Espanha': ['Andorra', 'França', 'Portugal'],
            'Estônia': ['Letônia'],
            'Finlândia': ['Noruega', 'Suécia'],
            'França': ['Andorra', 'Bélgica', 'Alemanha', 'Itália', 'Luxemburgo', 'Mônaco', 'Espanha', 'Suíça'],
            'Grécia': ['Albânia', 'Bulgária', 'Macedônia do Norte'],
            'Hungria': ['Áustria', 'Croácia', 'Romênia', 'Sérvia', 'Eslováquia', 'Eslovênia', 'Ucrânia'],
            'Inglaterra': ['Escócia', 'País de Gales'], ## REINO UNIDO
            'Irlanda': ['Escócia'], ## REINO UNIDO
            'Islândia': [],
            'Itália': ['Áustria', 'França', 'San Marino', 'Suíça', 'Eslovênia', 'Vaticano'],
            'Kosovo': ['Albânia', 'Macedônia do Norte', 'Montenegro', 'Sérvia'],
            'Letônia': ['Belarus', 'Estônia', 'Lituânia'],
            'Liechtenstein': ['Áustria', 'Suíça'],
            'Lituânia': ['Belarus', 'Letônia', 'Polônia'],
            'Luxemburgo': ['Bélgica', 'França', 'Alemanha'],
            'Malta': [],
            'Moldávia': ['Romênia', 'Ucrânia'],
            'Mônaco': ['França'],
            'Montenegro': ['Albânia', 'Bósnia e Herzegovina', 'Croácia', 'Kosovo', 'Sérvia'],
            'Macedônia do Norte': ['Albânia', 'Bulgária', 'Grécia', 'Kosovo', 'Sérvia'],
            'Noruega': ['Finlândia', 'Suécia'],
            'País de Gales': ['Inglaterra'], ## REINO UNIDO
            'Países Baixos': ['Bélgica', 'Alemanha'],
            'Polônia': ['Belarus', 'República Tcheca', 'Alemanha', 'Lituânia', 'Eslováquia', 'Ucrânia'],
            'Portugal': ['Espanha'],
            'República Tcheca': ['Áustria', 'Alemanha', 'Polônia', 'Eslováquia'],
            'Romênia': ['Bulgária', 'Hungria', 'Moldávia', 'Sérvia', 'Ucrânia'],
            'Rússia': ['Belarus', 'Estônia', 'Finlândia', 'Letônia', 'Ucrânia'],
            'San Marino': ['Itália'],
            'Sérvia': ['Bósnia e Herzegovina', 'Bulgária', 'Croácia', 'Hungria', 'Kosovo', 'Macedônia do Norte', 'Montenegro', 'Romênia'],
            'Suécia': ['Finlândia', 'Noruega'],
            'Suíça': ['Áustria', 'França', 'Alemanha', 'Itália', 'Liechtenstein'],
            'Ucrânia': ['Belarus', 'Hungria', 'Moldávia', 'Polônia', 'Romênia', 'Eslováquia'],
            'Vaticano': ['Itália']
        }

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
        paises_vizinhos = self.rotas.get(atual.pais)  
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
        print('Países visitados: ', qtdVisitados)
        print('Países expandidos: ', qtdExpandidos)
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
            resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, i, fronteira)
            if resultado is not None:
                self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)
                break

algbusca = BuscaAprofundamentoIterativo()
algbusca.realizaBusca('Alemanha','Croácia')