from queue import Queue

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
        self.rotas = {
            'Albania': ['Montenegro', 'Macedônia do Norte'],
            'Alemanha': ['França', 'Bélgica', 'Países Baixos', 'Dinamarca', 'Áustria', 'República Tcheca', 'Suíça'],
            'Andorra': ['Espanha', 'França'],
            'Áustria': ['Alemanha', 'República Tcheca', 'Eslováquia', 'Hungria', 'Suíça'],
            'Bélgica': ['França', 'Países Baixos', 'Alemanha', 'Luxemburgo'],
            'Bielorrússia': ['Polônia', 'Lituânia', 'Letônia', 'Ucrânia', 'Rússia'],
            'Bulgária': ['Romênia', 'Sérvia', 'Grécia', 'Macedônia do Norte'],
            'Croácia': ['Eslovênia', 'Hungria', 'Sérvia', 'Bósnia e Herzegovina', 'Montenegro'],
            'República Tcheca': ['Alemanha', 'Polônia', 'Áustria', 'Eslováquia'],
            'Dinamarca': ['Alemanha', 'Suécia'],
            'Eslováquia': ['República Tcheca', 'Polônia', 'Áustria', 'Hungria'],
            'Eslovênia': ['Áustria', 'Itália', 'Croácia', 'Hungria'],
            'Espanha': ['Portugal', 'França', 'Andorra'],
            'Estônia': ['Letônia', 'Finlândia', 'Rússia'],
            'Finlândia': ['Suécia', 'Estônia', 'Rússia'],
            'França': ['Bélgica', 'Luxemburgo', 'Alemanha', 'Suíça', 'Itália', 'Espanha', 'Inglaterra'],
            'Geórgia': ['Armênia', 'Azerbaijão', 'Turquia', 'Rússia'],
            'Grécia': ['Albânia', 'Macedônia do Norte', 'Bulgária', 'Turquia'],
            'Hungria': ['Áustria', 'Eslováquia', 'Ucrânia', 'Romênia', 'Sérvia', 'Croácia'],
            'Inglaterra': ['França'],  # Conexão da Inglaterra com a França
            'Itália': ['França', 'Suíça', 'Áustria', 'Eslovênia'],
            'Kosovo': ['Albânia', 'Sérvia', 'Montenegro'],
            'Letônia': ['Estônia', 'Lituânia', 'Bielorrússia', 'Rússia'],
            'Lituânia': ['Letônia', 'Polônia', 'Bielorrússia'],
            'Luxemburgo': ['Bélgica', 'França', 'Alemanha'],
            'Macedônia do Norte': ['Albânia', 'Grécia', 'Bulgária'],
            'Moldávia': ['Romênia', 'Ucrânia'],
            'Montenegro': ['Croácia', 'Bósnia e Herzegovina', 'Sérvia', 'Kosovo'],
            'Noruega': ['Suécia', 'Finlândia'],
            'Países Baixos': ['Bélgica', 'Alemanha'],
            'Polônia': ['Alemanha', 'República Tcheca', 'Eslováquia', 'Ucrânia', 'Lituânia'],
            'Portugal': ['Espanha'],
            'Romênia': ['Ucrânia', 'Moldávia', 'Bulgária', 'Hungria'],
            'Rússia': ['Finlândia', 'Estônia', 'Letônia', 'Lituânia', 'Bielorrússia', 'Ucrânia', 'Geórgia'],
            'Sérvia': ['Hungria', 'Romênia', 'Bósnia e Herzegovina', 'Montenegro', 'Kosovo'],
            'Suécia': ['Noruega', 'Dinamarca', 'Finlândia'],
            'Suíça': ['França', 'Alemanha', 'Áustria', 'Liechtenstein'],
            'Turquia': ['Grécia', 'Chipre', 'Geórgia', 'Armênia', 'Azerbaijão'],
            'Ucrânia': ['Polônia', 'República Tcheca', 'Eslováquia', 'Hungria', 'Romênia', 'Moldávia', 'Rússia']
        }

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
    def realizaBusca(self, origem, destino):
        fronteira = Queue()
        resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, fronteira)
        self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)

# Exemplo de execução
if __name__ == "__main__":
    algbusca = BuscaLargura()
    algbusca.realizaBusca('Alemanha', 'Hungria')
