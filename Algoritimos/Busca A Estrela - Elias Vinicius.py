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
#     self.rotas = {
#                   'Albânia': [('Macedônia do Norte', 160), ('Grécia', 440), ('Montenegro', 190)],
#                   'Alemanha': [('França', 875), ('Polônia', 575), ('Áustria', 525), ('Países Baixos', 655)],
#                   'Andorra': [('Espanha', 200), ('França', 125)],
#                   'Áustria': [('Alemanha', 525), ('Suíça', 725), ('Eslováquia', 55), ('Itália', 750)],
#                   'Bélgica': [('França', 315), ('Países Baixos', 210), ('Alemanha', 250)],
#                   'Bielorrússia': [('Ucrânia', 565), ('Polônia', 470), ('Lituânia', 180)],
#                   'Bósnia e Herzegovina': [('Croácia', 400), ('Sérvia', 300)],
#                   'Bulgária': [('Romênia', 335), ('Grécia', 525), ('Sérvia', 395)],
#                   'Croácia': [('Eslovênia', 140), ('Hungria', 345), ('Bósnia e Herzegovina', 400)],
#                   'Dinamarca': [('Alemanha', 350), ('Suécia', 650)],
#                   'Eslováquia': [('Áustria', 55), ('República Tcheca', 330), ('Polônia', 535)],
#                   'Eslovênia': [('Itália', 200), ('Áustria', 375), ('Croácia', 140)],
#                   'Espanha': [('França', 1035), ('Portugal', 625), ('Andorra', 200)],
#                   'Estônia': [('Letônia', 310), ('Finlândia', 80)],
#                   'Finlândia': [('Estônia', 80), ('Suécia', 395)],
#                   'França': [('Andorra', 125), ('Espanha', 1035), ('Bélgica', 315), ('Alemanha', 875), ('Suíça', 575)],
#                   'Grécia': [('Albânia', 440), ('Bulgária', 525)],
#                   'Hungria': [('Áustria', 243), ('Romênia', 815), ('Eslováquia', 200)],
#                   'Itália': [('França', 955), ('Suíça', 695), ('Áustria', 750), ('Eslovênia', 200), ('San Marino', 15)],
#                   'Kosovo': [('Macedônia do Norte', 120), ('Sérvia', 365)],
#                   'Letônia': [('Estônia', 310), ('Lituânia', 300)],
#                   'Liechtenstein': [('Suíça', 115), ('Áustria', 185)],
#                   'Lituânia': [('Letônia', 300), ('Polônia', 560), ('Bielorrússia', 180)],
#                   'Luxemburgo': [('Bélgica', 210), ('Alemanha', 250)],
#                   'Macedônia do Norte': [('Albânia', 160), ('Kosovo', 120), ('Sérvia', 440)],
#                   'Moldávia': [('Romênia', 450), ('Ucrânia', 260)],
#                   'Mônaco': [('França', 20)],
#                   'Montenegro': [('Albânia', 190), ('Sérvia', 470)],
#                   'Noruega': [('Suécia', 525), ('Dinamarca', 615)],
#                   'Países Baixos': [('Bélgica', 210), ('Alemanha', 655)],
#                   'Polônia': [('Alemanha', 575), ('Lituânia', 560), ('Ucrânia', 690), ('Eslováquia', 535)],
#                   'Portugal': [('Espanha', 625)],
#                   'República Tcheca': [('Alemanha', 360), ('Áustria', 250), ('Polônia', 625)],
#                   'Romênia': [('Bulgária', 335), ('Hungria', 815), ('Sérvia', 495), ('Moldávia', 450)],
#                   'Reino Unido': [('França', 345)],
#                   'San Marino': [('Itália', 15)],
#                   'Suécia': [('Dinamarca', 650), ('Finlândia', 395), ('Noruega', 525)],
#                   'Suíça': [('França', 575), ('Alemanha', 355), ('Itália', 695)],
#                   'Ucrânia': [('Polônia', 690), ('Bielorrússia', 565), ('Moldávia', 260)]
#                   }

            self.heuristicas= {
                  'Albânia': [('Albânia', 0), ('Alemanha', 1350), ('Andorra', 1600), ('Áustria', 950), ('Bélgica', 1750),
                        ('Bielorrússia', 1700), ('Bósnia e Herzegovina', 300), ('Bulgária', 400), ('Croácia', 600),
                        ('Dinamarca', 1800), ('Eslováquia', 900), ('Eslovênia', 500), ('Espanha', 1700), ('Estônia', 2000),
                        ('Finlândia', 2500), ('França', 1700), ('Grécia', 300), ('Hungria', 600), ('Itália', 800),
                        ('Kosovo', 200), ('Letônia', 2100), ('Liechtenstein', 900), ('Lituânia', 1900), ('Luxemburgo', 1700),
                        ('Macedônia do Norte', 150), ('Moldávia', 1000), ('Mônaco', 1300), ('Montenegro', 150),
                        ('Noruega', 2400), ('Países Baixos', 1800), ('Polônia', 1400), ('Portugal', 2000),
                        ('República Tcheca', 1100), ('Romênia', 600), ('Reino Unido', 2000), ('Suécia', 2200),
                        ('Suíça', 1300), ('Ucrânia', 1400), ('San Marino', 800)],

                'Alemanha': [('Albânia', 1350), ('Alemanha', 0), ('Andorra', 1250), ('Áustria', 500), ('Bélgica', 650),
                        ('Bielorrússia', 1050), ('Bósnia e Herzegovina', 1200), ('Bulgária', 1600), ('Croácia', 1000),
                        ('Dinamarca', 600), ('Eslováquia', 600), ('Eslovênia', 700), ('Espanha', 1500), ('Estônia', 1300),
                        ('Finlândia', 1700), ('França', 1000), ('Grécia', 1500), ('Hungria', 900), ('Itália', 880),
                        ('Kosovo', 1350), ('Letônia', 1300), ('Liechtenstein', 600), ('Lituânia', 1200), ('Luxemburgo', 600),
                        ('Macedônia do Norte', 1400), ('Moldávia', 1500), ('Mônaco', 1000), ('Montenegro', 1300),
                        ('Noruega', 900), ('Países Baixos', 450), ('Polônia', 600), ('Portugal', 2000),
                        ('República Tcheca', 300), ('Romênia', 1300), ('Reino Unido', 1000), ('Suécia', 1300),
                        ('Suíça', 650), ('Ucrânia', 1400), ('San Marino', 880)],

                'Andorra': [('Albânia', 1600), ('Alemanha', 1250), ('Andorra', 0), ('Áustria', 1350), ('Bélgica', 1000),
                        ('Bielorrússia', 2200), ('Bósnia e Herzegovina', 1400), ('Bulgária', 2000), ('Croácia', 1500),
                        ('Dinamarca', 1800), ('Eslováquia', 1600), ('Eslovênia', 1300), ('Espanha', 500), ('Estônia', 2700),
                        ('Finlândia', 3000), ('França', 800), ('Grécia', 2100), ('Hungria', 1700), ('Itália', 1000),
                        ('Kosovo', 1700), ('Letônia', 2500), ('Liechtenstein', 900), ('Lituânia', 2400), ('Luxemburgo', 950),
                        ('Macedônia do Norte', 1900), ('Moldávia', 2200), ('Mônaco', 500), ('Montenegro', 1600),
                        ('Noruega', 2400), ('Países Baixos', 1400), ('Polônia', 1600), ('Portugal', 1000),
                        ('República Tcheca', 1500), ('Romênia', 1900), ('Reino Unido', 1500), ('Suécia', 2300),
                        ('Suíça', 900), ('Ucrânia', 2300), ('San Marino', 1000)],

                'Áustria': [('Albânia', 950), ('Alemanha', 500), ('Andorra', 1350), ('Áustria', 0), ('Bélgica', 900),
                        ('Bielorrússia', 1100), ('Bósnia e Herzegovina', 600), ('Bulgária', 1000), ('Croácia', 400),
                        ('Dinamarca', 1000), ('Eslováquia', 250), ('Eslovênia', 300), ('Espanha', 1800), ('Estônia', 1400),
                        ('Finlândia', 1700), ('França', 1000), ('Grécia', 1300), ('Hungria', 200), ('Itália', 600),
                        ('Kosovo', 900), ('Letônia', 1400), ('Liechtenstein', 400), ('Lituânia', 1300), ('Luxemburgo', 750),
                        ('Macedônia do Norte', 1000), ('Moldávia', 1100), ('Mônaco', 900), ('Montenegro', 800),
                        ('Noruega', 1600), ('Países Baixos', 1000), ('Polônia', 500), ('Portugal', 2100),
                        ('República Tcheca', 200), ('Romênia', 900), ('Reino Unido', 1300), ('Suécia', 1700),
                        ('Suíça', 650), ('Ucrânia', 1100), ('San Marino', 600)],

                'Bélgica': [('Albânia', 1750), ('Alemanha', 650), ('Andorra', 1000), ('Áustria', 900), ('Bélgica', 0),
                        ('Bielorrússia', 1600), ('Bósnia e Herzegovina', 1500), ('Bulgária', 1800), ('Croácia', 1300),
                        ('Dinamarca', 800), ('Eslováquia', 1200), ('Eslovênia', 1200), ('Espanha', 1300), ('Estônia', 1800),
                        ('Finlândia', 1900), ('França', 300), ('Grécia', 2100), ('Hungria', 1300), ('Itália', 1100),
                        ('Kosovo', 1700), ('Letônia', 1700), ('Liechtenstein', 700), ('Lituânia', 1500), ('Luxemburgo', 200),
                        ('Macedônia do Norte', 1700), ('Moldávia', 1900), ('Mônaco', 1000), ('Montenegro', 1600),
                        ('Noruega', 1200), ('Países Baixos', 200), ('Polônia', 1100), ('Portugal', 1800),
                        ('República Tcheca', 800), ('Romênia', 1600), ('Reino Unido', 500), ('Suécia', 1400),
                        ('Suíça', 500), ('Ucrânia', 1600), ('San Marino', 1100)],

                'Bielorrússia': [('Albânia', 1700), ('Alemanha', 1050), ('Andorra', 2200), ('Áustria', 1100), ('Bélgica', 1600),
                        ('Bielorrússia', 0), ('Bósnia e Herzegovina', 1500), ('Bulgária', 1100), ('Croácia', 1200),
                        ('Dinamarca', 1200), ('Eslováquia', 800), ('Eslovênia', 1300), ('Espanha', 2500), ('Estônia', 500),
                        ('Finlândia', 800), ('França', 2000), ('Grécia', 1600), ('Hungria', 1000), ('Itália', 1500),
                        ('Kosovo', 1400), ('Letônia', 400), ('Liechtenstein', 1400), ('Lituânia', 300), ('Luxemburgo', 1700),
                        ('Macedônia do Norte', 1500), ('Moldávia', 500), ('Mônaco', 1900), ('Montenegro', 1400),
                        ('Noruega', 1200), ('Países Baixos', 1500), ('Polônia', 500), ('Portugal', 2700),
                        ('República Tcheca', 1000), ('Romênia', 700), ('Reino Unido', 1900), ('Suécia', 1300),
                        ('Suíça', 1400), ('Ucrânia', 400), ('San Marino', 1500)],

                'Bósnia e Herzegovina': [('Albânia', 300), ('Alemanha', 1200), ('Andorra', 1400), ('Áustria', 600), ('Bélgica', 1500),
                        ('Bielorrússia', 1500), ('Bósnia e Herzegovina', 0), ('Bulgária', 500), ('Croácia', 100),
                        ('Dinamarca', 1600), ('Eslováquia', 800), ('Eslovênia', 300), ('Espanha', 1600),
                        ('Estônia', 1800), ('Finlândia', 2200), ('França', 1600), ('Grécia', 700), ('Hungria', 300),
                        ('Itália', 500), ('Kosovo', 200), ('Letônia', 1700), ('Liechtenstein', 700), ('Lituânia', 1600),
                        ('Luxemburgo', 1300), ('Macedônia do Norte', 300), ('Moldávia', 900), ('Mônaco', 1000),
                        ('Montenegro', 100), ('Noruega', 2200), ('Países Baixos', 1500), ('Polônia', 1000),
                        ('Portugal', 2200), ('República Tcheca', 900), ('Romênia', 800), ('Reino Unido', 1800),
                        ('Suécia', 2000), ('Suíça', 1000), ('Ucrânia', 1200), ('San Marino', 500)],

                'Bulgária': [('Albânia', 400), ('Alemanha', 1600), ('Andorra', 2000), ('Áustria', 1000), ('Bélgica', 1800),
                        ('Bielorrússia', 1100), ('Bósnia e Herzegovina', 500), ('Bulgária', 0), ('Croácia', 600),
                        ('Dinamarca', 1900), ('Eslováquia', 1000), ('Eslovênia', 700), ('Espanha', 2300), ('Estônia', 1500),
                        ('Finlândia', 2000), ('França', 2000), ('Grécia', 400), ('Hungria', 700), ('Itália', 1000),
                        ('Kosovo', 300), ('Letônia', 1700), ('Liechtenstein', 1100), ('Lituânia', 1300), ('Luxemburgo', 1800),
                        ('Macedônia do Norte', 300), ('Moldávia', 500), ('Mônaco', 1400), ('Montenegro', 300),
                        ('Noruega', 2400), ('Países Baixos', 1700), ('Polônia', 1100), ('Portugal', 2700),
                        ('República Tcheca', 1300), ('Romênia', 300), ('Reino Unido', 2200), ('Suécia', 2100),
                        ('Suíça', 1300), ('Ucrânia', 700), ('San Marino', 900)],

                'Croácia': [('Albânia', 600), ('Alemanha', 1000), ('Andorra', 1500), ('Áustria', 400), ('Bélgica', 1300),
                        ('Bielorrússia', 1200), ('Bósnia e Herzegovina', 100), ('Bulgária', 600), ('Croácia', 0),
                        ('Dinamarca', 1400), ('Eslováquia', 600), ('Eslovênia', 100), ('Espanha', 1800), ('Estônia', 1600),
                        ('Finlândia', 2000), ('França', 1400), ('Grécia', 900), ('Hungria', 300), ('Itália', 400),
                        ('Kosovo', 400), ('Letônia', 1500), ('Liechtenstein', 600), ('Lituânia', 1400), ('Luxemburgo', 1200),
                        ('Macedônia do Norte', 500), ('Moldávia', 900), ('Mônaco', 1000), ('Montenegro', 300),
                        ('Noruega', 2100), ('Países Baixos', 1300), ('Polônia', 800), ('Portugal', 2000),
                        ('República Tcheca', 700), ('Romênia', 800), ('Reino Unido', 1700), ('Suécia', 1800),
                        ('Suíça', 800), ('Ucrânia', 1100), ('San Marino', 400)],

                'Dinamarca': [('Albânia', 1800), ('Alemanha', 600), ('Andorra', 1800), ('Áustria', 1000), ('Bélgica', 800),
                        ('Bielorrússia', 1200), ('Bósnia e Herzegovina', 1600), ('Bulgária', 1900), ('Croácia', 1400),
                        ('Dinamarca', 0), ('Eslováquia', 1000), ('Eslovênia', 1200), ('Espanha', 2200), ('Estônia', 1000),
                        ('Finlândia', 800), ('França', 1200), ('Grécia', 2100), ('Hungria', 1200), ('Itália', 1400),
                        ('Kosovo', 1700), ('Letônia', 900), ('Liechtenstein', 1200), ('Lituânia', 1000), ('Luxemburgo', 800),
                        ('Macedônia do Norte', 1700), ('Moldávia', 1400), ('Mônaco', 1400), ('Montenegro', 1600),
                        ('Noruega', 500), ('Países Baixos', 600), ('Polônia', 800), ('Portugal', 2200),
                        ('República Tcheca', 700), ('Romênia', 1600), ('Reino Unido', 1000), ('Suécia', 500),
                        ('Suíça', 1100), ('Ucrânia', 1500), ('San Marino', 1400)],

                'Eslováquia': [('Albânia', 900), ('Alemanha', 600), ('Andorra', 1500), ('Áustria', 300), ('Bélgica', 1100),
                        ('Bielorrússia', 800), ('Bósnia e Herzegovina', 800), ('Bulgária', 1000), ('Croácia', 600),
                        ('Dinamarca', 1000), ('Eslováquia', 0), ('Eslovênia', 400), ('Espanha', 1800), ('Estônia', 1200),
                        ('Finlândia', 1400), ('França', 1300), ('Grécia', 1300), ('Hungria', 200), ('Itália', 800),
                        ('Kosovo', 800), ('Letônia', 1100), ('Liechtenstein', 700), ('Lituânia', 900), ('Luxemburgo', 1000),
                        ('Macedônia do Norte', 900), ('Moldávia', 900), ('Mônaco', 1200), ('Montenegro', 800),
                        ('Noruega', 1600), ('Países Baixos', 1100), ('Polônia', 500), ('Portugal', 2100),
                        ('República Tcheca', 300), ('Romênia', 700), ('Reino Unido', 1600), ('Suécia', 1400),
                        ('Suíça', 900), ('Ucrânia', 800), ('San Marino', 800)],

                'Eslovênia': [('Albânia', 700), ('Alemanha', 600), ('Andorra', 1200), ('Áustria', 300), ('Bélgica', 1000),
                        ('Bielorrússia', 1300), ('Bósnia e Herzegovina', 300), ('Bulgária', 700), ('Croácia', 100),
                        ('Dinamarca', 1200), ('Eslováquia', 400), ('Eslovênia', 0), ('Espanha', 1600), ('Estônia', 1500),
                        ('Finlândia', 1900), ('França', 1200), ('Grécia', 1000), ('Hungria', 400), ('Itália', 400),
                        ('Kosovo', 600), ('Letônia', 1500), ('Liechtenstein', 600), ('Lituânia', 1300), ('Luxemburgo', 1000),
                        ('Macedônia do Norte', 700), ('Moldávia', 1200), ('Mônaco', 1000), ('Montenegro', 400),
                        ('Noruega', 1900), ('Países Baixos', 1200), ('Polônia', 900), ('Portugal', 2200),
                        ('República Tcheca', 500), ('Romênia', 900), ('Reino Unido', 1500), ('Suécia', 1600),
                        ('Suíça', 700), ('Ucrânia', 1000), ('San Marino', 300)],

                'Espanha': [('Albânia', 1900), ('Alemanha', 1500), ('Andorra', 200), ('Áustria', 1600), ('Bélgica', 1300),
                        ('Bielorrússia', 2500), ('Bósnia e Herzegovina', 1600), ('Bulgária', 2300), ('Croácia', 1800),
                        ('Dinamarca', 2200), ('Eslováquia', 1800), ('Eslovênia', 1600), ('Espanha', 0), ('Estônia', 2600),
                        ('Finlândia', 2800), ('França', 900), ('Grécia', 2400), ('Hungria', 2000), ('Itália', 1300),
                        ('Kosovo', 2100), ('Letônia', 2600), ('Liechtenstein', 1400), ('Lituânia', 2400), ('Luxemburgo', 1300),
                        ('Macedônia do Norte', 2100), ('Moldávia', 2400), ('Mônaco', 1000), ('Montenegro', 2000),
                        ('Noruega', 2900), ('Países Baixos', 1500), ('Polônia', 2200), ('Portugal', 400),
                        ('República Tcheca', 1800), ('Romênia', 2500), ('Reino Unido', 1400), ('Suécia', 2700),
                        ('Suíça', 1200), ('Ucrânia', 2700), ('San Marino', 1400)],

                'Estônia': [('Albânia', 2000), ('Alemanha', 1300), ('Andorra', 2400), ('Áustria', 1400), ('Bélgica', 1600),
                        ('Bielorrússia', 500), ('Bósnia e Herzegovina', 1800), ('Bulgária', 1500), ('Croácia', 1600),
                        ('Dinamarca', 1000), ('Eslováquia', 1200), ('Eslovênia', 1500), ('Espanha', 2600), ('Estônia', 0),
                        ('Finlândia', 80), ('França', 1900), ('Grécia', 2000), ('Hungria', 1400), ('Itália', 2000),
                        ('Kosovo', 1700), ('Letônia', 250), ('Liechtenstein', 1700), ('Lituânia', 500), ('Luxemburgo', 1600),
                        ('Macedônia do Norte', 1700), ('Moldávia', 1100), ('Mônaco', 2100), ('Montenegro', 1700),
                        ('Noruega', 1000), ('Países Baixos', 1500), ('Polônia', 900), ('Portugal', 3000),
                        ('República Tcheca', 1300), ('Romênia', 1500), ('Reino Unido', 2000), ('Suécia', 800),
                        ('Suíça', 1700), ('Ucrânia', 800), ('San Marino', 2000)],

                'Finlândia': [('Albânia', 2200), ('Alemanha', 1600), ('Andorra', 2800), ('Áustria', 1700), ('Bélgica', 1900),
                        ('Bielorrússia', 800), ('Bósnia e Herzegovina', 2200), ('Bulgária', 2000), ('Croácia', 2000),
                        ('Dinamarca', 800), ('Eslováquia', 1400), ('Eslovênia', 1900), ('Espanha', 2800), ('Estônia', 80),
                        ('Finlândia', 0), ('França', 2200), ('Grécia', 2400), ('Hungria', 1700), ('Itália', 2200),
                        ('Kosovo', 2100), ('Letônia', 700), ('Liechtenstein', 2000), ('Lituânia', 1000), ('Luxemburgo', 1900),
                        ('Macedônia do Norte', 2100), ('Moldávia', 1600), ('Mônaco', 2400), ('Montenegro', 2100),
                        ('Noruega', 500), ('Países Baixos', 1800), ('Polônia', 1200), ('Portugal', 3400),
                        ('República Tcheca', 1600), ('Romênia', 2000), ('Reino Unido', 2000), ('Suécia', 500),
                        ('Suíça', 2000), ('Ucrânia', 1200), ('San Marino', 2200)],

                'França': [('Albânia', 1600), ('Alemanha', 700), ('Andorra', 400), ('Áustria', 1000), ('Bélgica', 300),
                        ('Bielorrússia', 2000), ('Bósnia e Herzegovina', 1600), ('Bulgária', 2000), ('Croácia', 1400),
                        ('Dinamarca', 1200), ('Eslováquia', 1300), ('Eslovênia', 1200), ('Espanha', 900), ('Estônia', 1900),
                        ('Finlândia', 2200), ('França', 0), ('Grécia', 2100), ('Hungria', 1400), ('Itália', 900),
                        ('Kosovo', 1700), ('Letônia', 1700), ('Liechtenstein', 700), ('Lituânia', 1600), ('Luxemburgo', 200),
                        ('Macedônia do Norte', 1800), ('Moldávia', 2200), ('Mônaco', 300), ('Montenegro', 1600),
                        ('Noruega', 1800), ('Países Baixos', 500), ('Polônia', 1500), ('Portugal', 1200),
                        ('República Tcheca', 1100), ('Romênia', 2000), ('Reino Unido', 700), ('Suécia', 1600),
                        ('Suíça', 500), ('Ucrânia', 2000), ('San Marino', 1100)],

                'Grécia': [('Albânia', 300), ('Alemanha', 2000), ('Andorra', 1300), ('Áustria', 1200), ('Bélgica', 2000),
                      ('Bielorrússia', 2200), ('Bósnia e Herzegovina', 600), ('Bulgária', 300), ('Croácia', 500),
                      ('Dinamarca', 2000), ('Eslováquia', 1200), ('Eslovênia', 400), ('Espanha', 2400), ('Estônia', 2200),
                      ('Finlândia', 2400), ('França', 2100), ('Grécia', 0), ('Hungria', 900), ('Itália', 1000),
                      ('Kosovo', 100), ('Letônia', 1800), ('Liechtenstein', 1300), ('Lituânia', 1800), ('Luxemburgo', 2000),
                      ('Macedônia do Norte', 300), ('Moldávia', 1500), ('Mônaco', 1000), ('Montenegro', 200),
                      ('Noruega', 2400), ('Países Baixos', 2000), ('Polônia', 1800), ('Portugal', 2800),
                      ('República Tcheca', 1300), ('Romênia', 900), ('Reino Unido', 2500), ('Suécia', 2000),
                      ('Suíça', 1500), ('Ucrânia', 1500), ('San Marino', 900)],

                'Hungria': [('Albânia', 800), ('Alemanha', 800), ('Andorra', 1100), ('Áustria', 250), ('Bélgica', 900),
                      ('Bielorrússia', 1000), ('Bósnia e Herzegovina', 900), ('Bulgária', 900), ('Croácia', 200),
                      ('Dinamarca', 1300), ('Eslováquia', 150), ('Eslovênia', 300), ('Espanha', 1300), ('Estônia', 1500),
                      ('Finlândia', 1600), ('França', 1400), ('Grécia', 900), ('Hungria', 0), ('Itália', 700),
                      ('Kosovo', 400), ('Letônia', 1200), ('Liechtenstein', 700), ('Lituânia', 1100), ('Luxemburgo', 1000),
                      ('Macedônia do Norte', 700), ('Moldávia', 900), ('Mônaco', 1200), ('Montenegro', 700),
                      ('Noruega', 1700), ('Países Baixos', 1100), ('Polônia', 600), ('Portugal', 1900),
                      ('República Tcheca', 300), ('Romênia', 300), ('Reino Unido', 1600), ('Suécia', 1600),
                      ('Suíça', 600), ('Ucrânia', 800), ('San Marino', 700)],

                'Itália': [('Albânia', 800), ('Alemanha', 1000), ('Andorra', 1100), ('Áustria', 600), ('Bélgica', 1200),
                      ('Bielorrússia', 1600), ('Bósnia e Herzegovina', 700), ('Bulgária', 1100), ('Croácia', 300),
                      ('Dinamarca', 1400), ('Eslováquia', 800), ('Eslovênia', 200), ('Espanha', 1300), ('Estônia', 1900),
                      ('Finlândia', 2000), ('França', 900), ('Grécia', 1000), ('Hungria', 700), ('Itália', 0),
                      ('Kosovo', 600), ('Letônia', 1600), ('Liechtenstein', 600), ('Lituânia', 1300), ('Luxemburgo', 1200),
                      ('Macedônia do Norte', 600), ('Moldávia', 1400), ('Mônaco', 200), ('Montenegro', 300),
                      ('Noruega', 1800), ('Países Baixos', 1400), ('Polônia', 1100), ('Portugal', 1900),
                      ('República Tcheca', 800), ('Romênia', 1200), ('Reino Unido', 1500), ('Suécia', 1800),
                      ('Suíça', 600), ('Ucrânia', 1300), ('San Marino', 10)],

                'Kosovo': [('Albânia', 60), ('Alemanha', 1500), ('Andorra', 1700), ('Áustria', 600), ('Bélgica', 1500),
                      ('Bielorrússia', 1600), ('Bósnia e Herzegovina', 200), ('Bulgária', 700), ('Croácia', 300),
                      ('Dinamarca', 1700), ('Eslováquia', 900), ('Eslovênia', 600), ('Espanha', 1700), ('Estônia', 1900),
                      ('Finlândia', 2000), ('França', 1200), ('Grécia', 200), ('Hungria', 400), ('Itália', 600),
                      ('Kosovo', 0), ('Letônia', 1600), ('Liechtenstein', 1200), ('Lituânia', 1300), ('Luxemburgo', 1500),
                      ('Macedônia do Norte', 80), ('Moldávia', 1200), ('Mônaco', 1600), ('Montenegro', 200),
                      ('Noruega', 1900), ('Países Baixos', 1500), ('Polônia', 1300), ('Portugal', 2100),
                      ('República Tcheca', 800), ('Romênia', 1000), ('Reino Unido', 1700), ('Suécia', 1800),
                      ('Suíça', 1400), ('Ucrânia', 1300), ('San Marino', 600)],

                'Letônia': [('Albânia', 1900), ('Alemanha', 1300), ('Andorra', 2000), ('Áustria', 1400), ('Bélgica', 1500),
                      ('Bielorrússia', 600), ('Bósnia e Herzegovina', 1700), ('Bulgária', 1900), ('Croácia', 1600),
                      ('Dinamarca', 1200), ('Eslováquia', 1500), ('Eslovênia', 1600), ('Espanha', 2300), ('Estônia', 300),
                      ('Finlândia', 200), ('França', 1700), ('Grécia', 2000), ('Hungria', 1300), ('Itália', 1600),
                      ('Kosovo', 1700), ('Letônia', 0), ('Liechtenstein', 1600), ('Lituânia', 200), ('Luxemburgo', 1600),
                      ('Macedônia do Norte', 1800), ('Moldávia', 800), ('Mônaco', 1900), ('Montenegro', 1700),
                      ('Noruega', 1500), ('Países Baixos', 1400), ('Polônia', 900), ('Portugal', 2300),
                      ('República Tcheca', 1500), ('Romênia', 1900), ('Reino Unido', 2100), ('Suécia', 1200),
                      ('Suíça', 1500), ('Ucrânia', 700), ('San Marino', 1900)],

                'Liechtenstein': [('Albânia', 1200), ('Alemanha', 200), ('Andorra', 1200), ('Áustria', 100), ('Bélgica', 700),
                      ('Bielorrússia', 1500), ('Bósnia e Herzegovina', 1000), ('Bulgária', 1300), ('Croácia', 800),
                      ('Dinamarca', 1000), ('Eslováquia', 800), ('Eslovênia', 400), ('Espanha', 1400), ('Estônia', 1700),
                      ('Finlândia', 1800), ('França', 600), ('Grécia', 1300), ('Hungria', 600), ('Itália', 200),
                      ('Kosovo', 1100), ('Letônia', 1600), ('Liechtenstein', 0), ('Lituânia', 1300), ('Luxemburgo', 400),
                      ('Macedônia do Norte', 1300), ('Moldávia', 1400), ('Mônaco', 600), ('Montenegro', 600),
                      ('Noruega', 1700), ('Países Baixos', 800), ('Polônia', 1200), ('Portugal', 1500),
                      ('República Tcheca', 500), ('Romênia', 1300), ('Reino Unido', 1100), ('Suécia', 1500),
                      ('Suíça', 150), ('Ucrânia', 1400), ('San Marino', 900)],

                'Lituânia': [('Albânia', 1900), ('Alemanha', 1200), ('Andorra', 2000), ('Áustria', 1400), ('Bélgica', 1500),
                      ('Bielorrússia', 400), ('Bósnia e Herzegovina', 1600), ('Bulgária', 1600), ('Croácia', 1400),
                      ('Dinamarca', 1300), ('Eslováquia', 1500), ('Eslovênia', 1500), ('Espanha', 2300), ('Estônia', 100),
                      ('Finlândia', 200), ('França', 1700), ('Grécia', 2000), ('Hungria', 1200), ('Itália', 1300),
                      ('Kosovo', 1800), ('Letônia', 200), ('Liechtenstein', 1300), ('Lituânia', 0), ('Luxemburgo', 1700),
                      ('Macedônia do Norte', 1700), ('Moldávia', 800), ('Mônaco', 1900), ('Montenegro', 1700),
                      ('Noruega', 1800), ('Países Baixos', 1300), ('Polônia', 800), ('Portugal', 2200),
                      ('República Tcheca', 1500), ('Romênia', 1600), ('Reino Unido', 2000), ('Suécia', 1200),
                      ('Suíça', 1300), ('Ucrânia', 600), ('San Marino', 2000)],

                'Luxemburgo': [('Albânia', 1500), ('Alemanha', 200), ('Andorra', 1200), ('Áustria', 600), ('Bélgica', 200),
                      ('Bielorrússia', 1500), ('Bósnia e Herzegovina', 1400), ('Bulgária', 1600), ('Croácia', 1300),
                      ('Dinamarca', 900), ('Eslováquia', 800), ('Eslovênia', 900), ('Espanha', 1300), ('Estônia', 1600),
                      ('Finlândia', 1700), ('França', 200), ('Grécia', 2000), ('Hungria', 1000), ('Itália', 1200),
                      ('Kosovo', 1500), ('Letônia', 1600), ('Liechtenstein', 400), ('Lituânia', 1700), ('Luxemburgo', 0),
                      ('Macedônia do Norte', 1800), ('Moldávia', 1500), ('Mônaco', 800), ('Montenegro', 1300),
                      ('Noruega', 1700), ('Países Baixos', 400), ('Polônia', 1200), ('Portugal', 2000),
                      ('República Tcheca', 600), ('Romênia', 1400), ('Reino Unido', 1200), ('Suécia', 1600),
                      ('Suíça', 400), ('Ucrânia', 1400), ('San Marino', 1300)],

                'Macedônia do Norte': [('Albânia', 60), ('Alemanha', 1400), ('Andorra', 1700), ('Áustria', 800), ('Bélgica', 1700),
                      ('Bielorrússia', 1600), ('Bósnia e Herzegovina', 200), ('Bulgária', 150), ('Croácia', 300),
                      ('Dinamarca', 1400), ('Eslováquia', 1200), ('Eslovênia', 500), ('Espanha', 1700), ('Estônia', 2000),
                      ('Finlândia', 2100), ('França', 1500), ('Grécia', 300), ('Hungria', 700), ('Itália', 600),
                      ('Kosovo', 80), ('Letônia', 1800), ('Liechtenstein', 1200), ('Lituânia', 1700), ('Luxemburgo', 1800),
                      ('Macedônia do Norte', 0), ('Moldávia', 1200), ('Mônaco', 1600), ('Montenegro', 200),
                      ('Noruega', 1800), ('Países Baixos', 1600), ('Polônia', 1600), ('Portugal', 2000),
                      ('República Tcheca', 800), ('Romênia', 500), ('Reino Unido', 1700), ('Suécia', 1800),
                      ('Suíça', 800), ('Ucrânia', 600), ('San Marino', 600)],

                'Moldávia': [('Albânia', 1300), ('Alemanha', 1800), ('Andorra', 2000), ('Áustria', 1300), ('Bélgica', 2000),
                      ('Bielorrússia', 400), ('Bósnia e Herzegovina', 1500), ('Bulgária', 250), ('Croácia', 1300),
                      ('Dinamarca', 1600), ('Eslováquia', 1300), ('Eslovênia', 1400), ('Espanha', 2100), ('Estônia', 1700),
                      ('Finlândia', 1800), ('França', 1600), ('Grécia', 1300), ('Hungria', 900), ('Itália', 1400),
                      ('Kosovo', 1200), ('Letônia', 800), ('Liechtenstein', 1800), ('Lituânia', 800), ('Luxemburgo', 1600),
                      ('Macedônia do Norte', 1200), ('Moldávia', 0), ('Mônaco', 2000), ('Montenegro', 1300),
                      ('Noruega', 1700), ('Países Baixos', 1700), ('Polônia', 1400), ('Portugal', 2200),
                      ('República Tcheca', 1300), ('Romênia', 250), ('Reino Unido', 2100), ('Suécia', 1900),
                      ('Suíça', 1500), ('Ucrânia', 500), ('San Marino', 1800)],

                'Mônaco': [('Albânia', 1200), ('Alemanha', 1000), ('Andorra', 150), ('Áustria', 700), ('Bélgica', 800),
                      ('Bielorrússia', 1300), ('Bósnia e Herzegovina', 900), ('Bulgária', 1200), ('Croácia', 400),
                      ('Dinamarca', 1300), ('Eslováquia', 1100), ('Eslovênia', 400), ('Espanha', 600), ('Estônia', 1300),
                      ('Finlândia', 1400), ('França', 0), ('Grécia', 1000), ('Hungria', 600), ('Itália', 200),
                      ('Kosovo', 1100), ('Letônia', 1500), ('Liechtenstein', 700), ('Lituânia', 1300), ('Luxemburgo', 800),
                      ('Macedônia do Norte', 1200), ('Moldávia', 1300), ('Mônaco', 0), ('Montenegro', 300),
                      ('Noruega', 1500), ('Países Baixos', 1300), ('Polônia', 1400), ('Portugal', 1300),
                      ('República Tcheca', 800), ('Romênia', 1200), ('Reino Unido', 1200), ('Suécia', 1400),
                      ('Suíça', 200), ('Ucrânia', 1400), ('San Marino', 1000)],

                'Montenegro': [('Albânia', 60), ('Alemanha', 1100), ('Andorra', 1200), ('Áustria', 900), ('Bélgica', 1300),
                      ('Bielorrússia', 1400), ('Bósnia e Herzegovina', 200), ('Bulgária', 1200), ('Croácia', 100),
                      ('Dinamarca', 1400), ('Eslováquia', 1200), ('Eslovênia', 300), ('Espanha', 1300), ('Estônia', 1600),
                      ('Finlândia', 1700), ('França', 1300), ('Grécia', 400), ('Hungria', 700), ('Itália', 300),
                      ('Kosovo', 200), ('Letônia', 1700), ('Liechtenstein', 1300), ('Lituânia', 1600), ('Luxemburgo', 1300),
                      ('Macedônia do Norte', 200), ('Moldávia', 1300), ('Mônaco', 300), ('Montenegro', 0),
                      ('Noruega', 1700), ('Países Baixos', 1300), ('Polônia', 1400), ('Portugal', 1500),
                      ('República Tcheca', 900), ('Romênia', 1200), ('Reino Unido', 1400), ('Suécia', 1600),
                      ('Suíça', 800), ('Ucrânia', 1300), ('San Marino', 300)],

                'Noruega': [('Albânia', 2000), ('Alemanha', 1200), ('Andorra', 1700), ('Áustria', 1400), ('Bélgica', 1500),
                      ('Bielorrússia', 1700), ('Bósnia e Herzegovina', 1800), ('Bulgária', 1900), ('Croácia', 1600),
                      ('Dinamarca', 600), ('Eslováquia', 1600), ('Eslovênia', 1800), ('Espanha', 1700), ('Estônia', 1600),
                      ('Finlândia', 600), ('França', 1600), ('Grécia', 2000), ('Hungria', 1800), ('Itália', 1800),
                      ('Kosovo', 1900), ('Letônia', 1600), ('Liechtenstein', 1600), ('Lituânia', 1900), ('Luxemburgo', 1700),
                      ('Macedônia do Norte', 2000), ('Moldávia', 1700), ('Mônaco', 2000), ('Montenegro', 1800),
                      ('Noruega', 0), ('Países Baixos', 1400), ('Polônia', 1600), ('Portugal', 2200),
                      ('República Tcheca', 1600), ('Romênia', 2000), ('Reino Unido', 1500), ('Suécia', 500),
                      ('Suíça', 1300), ('Ucrânia', 1900), ('San Marino', 2000)],

                'Países Baixos': [('Albânia', 1400), ('Alemanha', 600), ('Andorra', 1200), ('Áustria', 900), ('Bélgica', 200),
                      ('Bielorrússia', 1300), ('Bósnia e Herzegovina', 1500), ('Bulgária', 1600), ('Croácia', 1400),
                      ('Dinamarca', 500), ('Eslováquia', 900), ('Eslovênia', 1000), ('Espanha', 1500), ('Estônia', 1200),
                      ('Finlândia', 1300), ('França', 600), ('Grécia', 2000), ('Hungria', 900), ('Itália', 1200),
                      ('Kosovo', 1600), ('Letônia', 1300), ('Liechtenstein', 800), ('Lituânia', 1400), ('Luxemburgo', 400),
                      ('Macedônia do Norte', 1600), ('Moldávia', 1300), ('Mônaco', 1300), ('Montenegro', 1400),
                      ('Noruega', 1400), ('Países Baixos', 0), ('Polônia', 800), ('Portugal', 1500),
                      ('República Tcheca', 1000), ('Romênia', 1300), ('Reino Unido', 700), ('Suécia', 1200),
                      ('Suíça', 600), ('Ucrânia', 1400), ('San Marino', 1400)],

                'Polônia': [('Albânia', 1400), ('Alemanha', 600), ('Andorra', 1600), ('Áustria', 800), ('Bélgica', 900),
                      ('Bielorrússia', 300), ('Bósnia e Herzegovina', 1200), ('Bulgária', 1300), ('Croácia', 1100),
                      ('Dinamarca', 700), ('Eslováquia', 300), ('Eslovênia', 800), ('Espanha', 1700), ('Estônia', 900),
                      ('Finlândia', 1100), ('França', 1200), ('Grécia', 1600), ('Hungria', 600), ('Itália', 1200),
                      ('Kosovo', 1600), ('Letônia', 800), ('Liechtenstein', 1000), ('Lituânia', 600), ('Luxemburgo', 1100),
                      ('Macedônia do Norte', 1600), ('Moldávia', 800), ('Mônaco', 1500), ('Montenegro', 1200),
                      ('Noruega', 1200), ('Países Baixos', 800), ('Polônia', 0), ('Portugal', 2000),
                      ('República Tcheca', 500), ('Romênia', 1200), ('Reino Unido', 1400), ('Suécia', 1200),
                      ('Suíça', 1100), ('Ucrânia', 500), ('San Marino', 1500)],

                'Portugal': [('Albânia', 2000), ('Alemanha', 1600), ('Andorra', 1300), ('Áustria', 1500), ('Bélgica', 1600),
                      ('Bielorrússia', 2000), ('Bósnia e Herzegovina', 1600), ('Bulgária', 1800), ('Croácia', 1900),
                      ('Dinamarca', 1600), ('Eslováquia', 1900), ('Eslovênia', 1700), ('Espanha', 600), ('Estônia', 2000),
                      ('Finlândia', 2200), ('França', 1300), ('Grécia', 2000), ('Hungria', 2000), ('Itália', 2000),
                      ('Kosovo', 2000), ('Letônia', 2000), ('Liechtenstein', 2000), ('Lituânia', 2100), ('Luxemburgo', 2000),
                      ('Macedônia do Norte', 2000), ('Moldávia', 2100), ('Mônaco', 1500), ('Montenegro', 1900),
                      ('Noruega', 2000), ('Países Baixos', 1700), ('Polônia', 2000), ('Portugal', 0),
                      ('República Tcheca', 1800), ('Romênia', 2000), ('Reino Unido', 2000), ('Suécia', 2000),
                      ('Suíça', 1500), ('Ucrânia', 2100), ('San Marino', 2000)],

                'República Tcheca': [('Albânia', 1200), ('Alemanha', 200), ('Andorra', 1300), ('Áustria', 250), ('Bélgica', 800),
                      ('Bielorrússia', 1300), ('Bósnia e Herzegovina', 1200), ('Bulgária', 1200), ('Croácia', 700),
                      ('Dinamarca', 1000), ('Eslováquia', 200), ('Eslovênia', 400), ('Espanha', 1100), ('Estônia', 1300),
                      ('Finlândia', 1400), ('França', 900), ('Grécia', 1500), ('Hungria', 300), ('Itália', 800),
                      ('Kosovo', 900), ('Letônia', 1200), ('Liechtenstein', 800), ('Lituânia', 1200), ('Luxemburgo', 700),
                      ('Macedônia do Norte', 900), ('Moldávia', 1100), ('Mônaco', 1300), ('Montenegro', 700),
                      ('Noruega', 1300), ('Países Baixos', 1000), ('Polônia', 500), ('Portugal', 1800),
                      ('República Tcheca', 0), ('Romênia', 1300), ('Reino Unido', 1200), ('Suécia', 1300),
                      ('Suíça', 800), ('Ucrânia', 1100), ('San Marino', 900)],

                'Romênia': [('Albânia', 300), ('Alemanha', 1400), ('Andorra', 1500), ('Áustria', 900), ('Bélgica', 1400),
                      ('Bielorrússia', 1400), ('Bósnia e Herzegovina', 1200), ('Bulgária', 100), ('Croácia', 1100),
                      ('Dinamarca', 1500), ('Eslováquia', 500), ('Eslovênia', 800), ('Espanha', 1900), ('Estônia', 1700),
                      ('Finlândia', 1900), ('França', 1200), ('Grécia', 900), ('Hungria', 100), ('Itália', 1300),
                      ('Kosovo', 1400), ('Letônia', 1400), ('Liechtenstein', 1300), ('Lituânia', 1600), ('Luxemburgo', 1400),
                      ('Macedônia do Norte', 500), ('Moldávia', 300), ('Mônaco', 2000), ('Montenegro', 900),
                      ('Noruega', 2000), ('Países Baixos', 1800), ('Polônia', 1100), ('Portugal', 2000),
                      ('República Tcheca', 1300), ('Romênia', 0), ('Reino Unido', 1200), ('Suécia', 2000),
                      ('Suíça', 1300), ('Ucrânia', 300), ('San Marino', 1200)],

                'Reino Unido': [('Albânia', 1700), ('Alemanha', 600), ('Andorra', 1300), ('Áustria', 1200), ('Bélgica', 700),
                      ('Bielorrússia', 1700), ('Bósnia e Herzegovina', 1400), ('Bulgária', 1300), ('Croácia', 1100),
                      ('Dinamarca', 1400), ('Eslováquia', 1300), ('Eslovênia', 1300), ('Espanha', 1500), ('Estônia', 1300),
                      ('Finlândia', 2000), ('França', 1400), ('Grécia', 1700), ('Hungria', 1500), ('Itália', 1100),
                      ('Kosovo', 1400), ('Letônia', 1800), ('Liechtenstein', 1300), ('Lituânia', 1400), ('Luxemburgo', 600),
                      ('Macedônia do Norte', 1600), ('Moldávia', 1300), ('Mônaco', 1400), ('Montenegro', 1300),
                      ('Noruega', 1500), ('Países Baixos', 800), ('Polônia', 1400), ('Portugal', 1600),
                      ('República Tcheca', 1300), ('Romênia', 1300), ('Reino Unido', 0), ('Suécia', 1400),
                      ('Suíça', 1100), ('Ucrânia', 1700), ('San Marino', 1300)],

                'San Marino': [('Albânia', 800), ('Alemanha', 880), ('Andorra', 1000), ('Áustria', 600), ('Bélgica', 1100),
                        ('Bielorrússia', 1500), ('Bósnia e Herzegovina', 500), ('Bulgária', 900), ('Croácia', 400),
                        ('Dinamarca', 1400), ('Eslováquia', 900), ('Eslovênia', 300), ('Espanha', 1500), ('Estônia', 1800),
                        ('Finlândia', 2100), ('França', 1000), ('Grécia', 1000), ('Hungria', 700), ('Itália', 0),
                        ('Kosovo', 500), ('Letônia', 1700), ('Liechtenstein', 700), ('Lituânia', 1600), ('Luxemburgo', 900),
                        ('Macedônia do Norte', 800), ('Moldávia', 1300), ('Mônaco', 500), ('Montenegro', 600),
                        ('Noruega', 2000), ('Países Baixos', 1200), ('Polônia', 1100), ('Portugal', 2000),
                        ('República Tcheca', 1000), ('Romênia', 1000), ('Reino Unido', 1500), ('Suécia', 1700),
                        ('Suíça', 600), ('Ucrânia', 1400), ('San Marino', 0)],

                'Suécia': [('Albânia', 2000), ('Alemanha', 1400), ('Andorra', 1500), ('Áustria', 1500), ('Bélgica', 1300),
                      ('Bielorrússia', 1600), ('Bósnia e Herzegovina', 1900), ('Bulgária', 1300), ('Croácia', 1700),
                      ('Dinamarca', 1000), ('Eslováquia', 1300), ('Eslovênia', 1700), ('Espanha', 1600), ('Estônia', 1400),
                      ('Finlândia', 900), ('França', 1400), ('Grécia', 2000), ('Hungria', 1700), ('Itália', 1600),
                      ('Kosovo', 1500), ('Letônia', 1900), ('Liechtenstein', 1700), ('Lituânia', 1100), ('Luxemburgo', 1300),
                      ('Macedônia do Norte', 2000), ('Moldávia', 1700), ('Mônaco', 2000), ('Montenegro', 1800),
                      ('Noruega', 500), ('Países Baixos', 1100), ('Polônia', 1600), ('Portugal', 2000),
                      ('República Tcheca', 1300), ('Romênia', 2000), ('Reino Unido', 1400), ('Suécia', 0),
                      ('Suíça', 1400), ('Ucrânia', 2000), ('San Marino', 1800)],

                'Suíça': [('Albânia', 1400), ('Alemanha', 400), ('Andorra', 1600), ('Áustria', 900), ('Bélgica', 700),
                      ('Bielorrússia', 1300), ('Bósnia e Herzegovina', 800), ('Bulgária', 2000), ('Croácia', 1400),
                      ('Dinamarca', 700), ('Eslováquia', 1600), ('Eslovênia', 800), ('Espanha', 1400), ('Estônia', 1700),
                      ('Finlândia', 800), ('França', 500), ('Grécia', 1600), ('Hungria', 1400), ('Itália', 900),
                      ('Kosovo', 1600), ('Letônia', 1300), ('Liechtenstein', 400), ('Lituânia', 1300), ('Luxemburgo', 300),
                      ('Macedônia do Norte', 700), ('Moldávia', 1800), ('Mônaco', 500), ('Montenegro', 1100),
                      ('Noruega', 800), ('Países Baixos', 600), ('Polônia', 1300), ('Portugal', 1400),
                      ('República Tcheca', 700), ('Romênia', 1400), ('Reino Unido', 1100), ('Suécia', 1200),
                      ('Suíça', 0), ('Ucrânia', 1700), ('San Marino', 1200)],

                'Ucrânia': [('Albânia', 1500), ('Alemanha', 1400), ('Andorra', 1500), ('Áustria', 1600), ('Bélgica', 1200),
                      ('Bielorrússia', 200), ('Bósnia e Herzegovina', 1300), ('Bulgária', 1100), ('Croácia', 1600),
                      ('Dinamarca', 1300), ('Eslováquia', 1200), ('Eslovênia', 1400), ('Espanha', 1500), ('Estônia', 600),
                      ('Finlândia', 1300), ('França', 1300), ('Grécia', 2000), ('Hungria', 1600), ('Itália', 1700),
                      ('Kosovo', 1400), ('Letônia', 700), ('Liechtenstein', 1000), ('Lituânia', 600), ('Luxemburgo', 900),
                      ('Macedônia do Norte', 400), ('Moldávia', 600), ('Mônaco', 2000), ('Montenegro', 1300),
                      ('Noruega', 1600), ('Países Baixos', 1300), ('Polônia', 300), ('Portugal', 2000),
                      ('República Tcheca', 1100), ('Romênia', 300), ('Reino Unido', 1300), ('Suécia', 600),
                      ('Suíça', 1700), ('Ucrânia', 0), ('San Marino', 1300)]
                  }

      def realizaBusca(self, origem, destino):
            fronteira = []
            resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, fronteira)
            self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)

      def busca(self, origem, destino, fronteira):
            distancias = self.heuristicas.get(origem)
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
      algbusca.realizaBusca('Lisbon','Berlin')