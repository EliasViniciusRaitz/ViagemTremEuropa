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
    self.rotas = {
                  'Tirana': [('Skopje', 160), ('Atenas', 440), ('Podgorica', 190)],
                  'Berlim': [('Paris', 875), ('Varsóvia', 575), ('Viena', 525), ('Amsterdã', 655)],
                  'Andorra-a-Velha': [('Madri', 200), ('Paris', 125)],
                  'Viena': [('Berlim', 525), ('Berna', 725), ('Bratislava', 55), ('Roma', 750)],
                  'Bruxelas': [('Paris', 315), ('Amsterdã', 210), ('Berlim', 250)],
                  'Minsk': [('Kiev', 565), ('Varsóvia', 470), ('Vilnius', 180)],
                  'Sarajevo': [('Zagreb', 400), ('Belgrado', 300)],
                  'Sófia': [('Bucareste', 335), ('Atenas', 525), ('Belgrado', 395)],
                  'Zagreb': [('Liubliana', 140), ('Budapeste', 345), ('Sarajevo', 400)],
                  'Copenhague': [('Berlim', 350), ('Estocolmo', 650)],
                  'Bratislava': [('Viena', 55), ('Praga', 330), ('Varsóvia', 535)],
                  'Liubliana': [('Roma', 200), ('Viena', 375), ('Zagreb', 140)],
                  'Madri': [('Paris', 1035), ('Lisboa', 625), ('Andorra-a-Velha', 200)],
                  'Tallinn': [('Riga', 310), ('Helsinque', 80)],
                  'Helsinque': [('Tallinn', 80), ('Estocolmo', 395)],
                  'Paris': [('Andorra-a-Velha', 125), ('Madri', 1035), ('Bruxelas', 315), ('Berlim', 875), ('Berna', 575)],
                  'Atenas': [('Tirana', 440), ('Sófia', 525)],
                  'Budapeste': [('Viena', 243), ('Bucareste', 815), ('Bratislava', 200)],
                  'Roma': [('Paris', 955), ('Berna', 695), ('Viena', 750), ('Liubliana', 200), ('San Marino', 15)],
                  'Pristina': [('Skopje', 120), ('Belgrado', 365)],
                  'Riga': [('Tallinn', 310), ('Vilnius', 300)],
                  'Vaduz': [('Berna', 115), ('Viena', 185)],
                  'Vilnius': [('Riga', 300), ('Varsóvia', 560), ('Minsk', 180)],
                  'Luxemburgo': [('Bruxelas', 210), ('Berlim', 250)],
                  'Skopje': [('Tirana', 160), ('Pristina', 120), ('Belgrado', 440)],
                  'Chisinau': [('Bucareste', 450), ('Kiev', 260)],
                  'Mônaco': [('Paris', 20)],
                  'Podgorica': [('Tirana', 190), ('Belgrado', 470)],
                  'Oslo': [('Estocolmo', 525), ('Copenhague', 615)],
                  'Amsterdã': [('Bruxelas', 210), ('Berlim', 655)],
                  'Varsóvia': [('Berlim', 575), ('Vilnius', 560), ('Kiev', 690), ('Bratislava', 535)],
                  'Lisboa': [('Madri', 625)],
                  'Praga': [('Berlim', 360), ('Viena', 250), ('Varsóvia', 625)],
                  'Bucareste': [('Sófia', 335), ('Budapeste', 815), ('Belgrado', 495), ('Chisinau', 450)],
                  'Londres': [('Paris', 345)],
                  'San Marino': [('Roma', 15)],
                  'Estocolmo': [('Copenhague', 650), ('Helsinque', 395), ('Oslo', 525)],
                  'Berna': [('Paris', 575), ('Berlim', 355), ('Roma', 695)],
                  'Kiev': [('Varsóvia', 690), ('Minsk', 565), ('Chisinau', 260)],
                  }
    self.heuristicas= {
                  'Tirana': [('Tirana', 0), ('Berlim', 1350), ('Andorra-a-Velha', 1600), ('Viena', 950), ('Bruxelas', 1750), 
                        ('Minsk', 1700), ('Sarajevo', 300), ('Sófia', 400), ('Zagreb', 600),
                        ('Copenhague', 1800), ('Bratislava', 900), ('Liubliana', 500), ('Madri', 1700), ('Tallinn', 2000),
                        ('Helsinque', 2500), ('Paris', 1700), ('Atenas', 300), ('Budapeste', 600), ('Roma', 800),
                        ('Pristina', 200), ('Riga', 2100), ('Vaduz', 900), ('Vilnius', 1900), ('Luxemburgo', 1700),
                        ('Skopje', 150), ('Chisinau', 1000), ('Mônaco', 1300), ('Podgorica', 150),
                        ('Oslo', 2400), ('Amsterdã', 1800), ('Varsóvia', 1400), ('Lisboa', 2000),
                        ('Praga', 1100), ('Bucareste', 600), ('Londres', 2000), ('Estocolmo', 2200),
                        ('Berna', 1300), ('Kiev', 1400), ('San Marino', 800)],

                  'Berlim': [('Tirana', 1350), ('Berlim', 0), ('Andorra-a-Velha', 1250), ('Viena', 500), ('Bruxelas', 650),
                        ('Minsk', 1050), ('Sarajevo', 1200), ('Sófia', 1600), ('Zagreb', 1000),
                        ('Copenhague', 600), ('Bratislava', 600), ('Liubliana', 700), ('Madri', 1500), ('Tallinn', 1300),
                        ('Helsinque', 1700), ('Paris', 1000), ('Atenas', 1500), ('Budapeste', 900), ('Roma', 880),
                        ('Pristina', 1350), ('Riga', 1300), ('Vaduz', 600), ('Vilnius', 1200), ('Luxemburgo', 600),
                        ('Skopje', 1400), ('Chisinau', 1500), ('Mônaco', 1000), ('Podgorica', 1300),
                        ('Oslo', 900), ('Amsterdã', 450), ('Varsóvia', 600), ('Lisboa', 2000),
                        ('Praga', 300), ('Bucareste', 1300), ('Londres', 1000), ('Estocolmo', 1300),
                        ('Berna', 650), ('Kiev', 1400), ('San Marino', 880)],

                  'Andorra-a-Velha': [('Tirana', 1600), ('Berlim', 1250), ('Andorra-a-Velha', 0), ('Viena', 1350), ('Bruxelas', 1000),
                        ('Minsk', 2200), ('Sarajevo', 1400), ('Sófia', 2000), ('Zagreb', 1500),
                        ('Copenhague', 1800), ('Bratislava', 1600), ('Liubliana', 1300), ('Madri', 500), ('Tallinn', 2700),
                        ('Helsinque', 3000), ('Paris', 800), ('Atenas', 2100), ('Budapeste', 1700), ('Roma', 1000),
                        ('Pristina', 1700), ('Riga', 2500), ('Vaduz', 900), ('Vilnius', 2400), ('Luxemburgo', 950),
                        ('Skopje', 1900), ('Chisinau', 2200), ('Mônaco', 500), ('Podgorica', 1600),
                        ('Oslo', 2400), ('Amsterdã', 1400), ('Varsóvia', 1600), ('Lisboa', 1000),
                        ('Praga', 1500), ('Bucareste', 1900), ('Londres', 1500), ('Estocolmo', 2300),
                        ('Berna', 900), ('Kiev', 2300), ('San Marino', 1000)],

                  'Viena': [('Tirana', 950), ('Berlim', 500), ('Andorra-a-Velha', 1350), ('Viena', 0), ('Bruxelas', 900),
                        ('Minsk', 1100), ('Sarajevo', 600), ('Sófia', 1000), ('Zagreb', 400),
                        ('Copenhague', 1000), ('Bratislava', 250), ('Liubliana', 300), ('Madri', 1800), ('Tallinn', 1400),
                        ('Helsinque', 1700), ('Paris', 1000), ('Atenas', 1300), ('Budapeste', 200), ('Roma', 600),
                        ('Pristina', 900), ('Riga', 1400), ('Vaduz', 400), ('Vilnius', 1300), ('Luxemburgo', 750),
                        ('Skopje', 1000), ('Chisinau', 1100), ('Mônaco', 900), ('Podgorica', 800),
                        ('Oslo', 1600), ('Amsterdã', 1000), ('Varsóvia', 500), ('Lisboa', 2100),
                        ('Praga', 200), ('Bucareste', 900), ('Londres', 1300), ('Estocolmo', 1700),
                        ('Berna', 650), ('Kiev', 1100), ('San Marino', 600)],

                  'Bruxelas': [('Tirana', 1750), ('Berlim', 650), ('Andorra-a-Velha', 1000), ('Viena', 900), ('Bruxelas', 0),
                        ('Minsk', 2000), ('Sarajevo', 1400), ('Sófia', 1700), ('Zagreb', 1200),
                        ('Copenhague', 1000), ('Bratislava', 950), ('Liubliana', 1300), ('Madri', 1300), ('Tallinn', 2200),
                        ('Helsinque', 2500), ('Paris', 300), ('Atenas', 1800), ('Budapeste', 1300), ('Roma', 1300),
                        ('Pristina', 1700), ('Riga', 2100), ('Vaduz', 1300), ('Vilnius', 1800), ('Luxemburgo', 350),
                        ('Skopje', 1700), ('Chisinau', 2000), ('Mônaco', 1600), ('Podgorica', 1500),
                        ('Oslo', 1300), ('Amsterdã', 170), ('Varsóvia', 1300), ('Lisboa', 1800),
                        ('Praga', 800), ('Bucareste', 1500), ('Londres', 300), ('Estocolmo', 1500),
                        ('Berna', 900), ('Kiev', 1700), ('San Marino', 1300)],

                  'Minsk': [('Tirana', 1700), ('Berlim', 1050), ('Andorra-a-Velha', 2200), ('Viena', 1100), ('Bruxelas', 2000),
                        ('Minsk', 0), ('Sarajevo', 1600), ('Sófia', 2100), ('Zagreb', 1500),
                        ('Copenhague', 1600), ('Bratislava', 1400), ('Liubliana', 1700), ('Madri', 2200), ('Tallinn', 900),
                        ('Helsinque', 1200), ('Paris', 2100), ('Atenas', 2300), ('Budapeste', 1700), ('Roma', 2000),
                        ('Pristina', 2000), ('Riga', 600), ('Vaduz', 1500), ('Vilnius', 400), ('Luxemburgo', 2200),
                        ('Skopje', 2400), ('Chisinau', 600), ('Mônaco', 2000), ('Podgorica', 2100),
                        ('Oslo', 1900), ('Amsterdã', 1500), ('Varsóvia', 600), ('Lisboa', 2500),
                        ('Praga', 1400), ('Bucareste', 2300), ('Londres', 2000), ('Estocolmo', 1600),
                        ('Berna', 1700), ('Kiev', 300), ('San Marino', 2000)],

                  'Saravejo': [('Tirana', 300), ('Berlim', 1200), ('Andorra-a-Velha', 1400), ('Viena', 600), ('Bruxelas', 1400),
                        ('Minsk', 1600), ('Sarajevo', 0), ('Sófia', 1300), ('Zagreb', 200),
                        ('Copenhague', 1400), ('Bratislava', 850), ('Liubliana', 300), ('Madri', 1600), ('Tallinn', 1900),
                        ('Helsinque', 2100), ('Paris', 1200), ('Atenas', 1200), ('Budapeste', 600), ('Roma', 700),
                        ('Pristina', 400), ('Riga', 1900), ('Vaduz', 800), ('Vilnius', 1800), ('Luxemburgo', 1400),
                        ('Skopje', 300), ('Chisinau', 1700), ('Mônaco', 1300), ('Podgorica', 150),
                        ('Oslo', 1900), ('Amsterdã', 1300), ('Varsóvia', 1200), ('Lisboa', 1700),
                        ('Praga', 450), ('Bucareste', 1300), ('Londres', 1400), ('Estocolmo', 1900),
                        ('Berna', 800), ('Kiev', 1500), ('San Marino', 700)],

                  'Sófia': [('Tirana', 400), ('Berlim', 1600), ('Andorra-a-Velha', 2000), ('Viena', 1000), ('Bruxelas', 1700),
                        ('Minsk', 2100), ('Sarajevo', 1300), ('Sófia', 0), ('Zagreb', 1300),
                        ('Copenhague', 1800), ('Bratislava', 1000), ('Liubliana', 1400), ('Madri', 2000), ('Tallinn', 2100),
                        ('Helsinque', 2400), ('Paris', 1700), ('Atenas', 300), ('Budapeste', 600), ('Roma', 1200),
                        ('Pristina', 700), ('Riga', 2200), ('Vaduz', 1400), ('Vilnius', 2200), ('Luxemburgo', 1700),
                        ('Skopje', 1000), ('Chisinau', 1000), ('Mônaco', 1700), ('Podgorica', 1100),
                        ('Oslo', 2400), ('Amsterdã', 1600), ('Varsóvia', 1300), ('Lisboa', 2200),
                        ('Praga', 1300), ('Bucareste', 300), ('Londres', 1800), ('Estocolmo', 2200),
                        ('Berna', 1400), ('Kiev', 2000), ('San Marino', 1200)],

                  'Zagreb': [('Tirana', 600), ('Berlim', 1000), ('Andorra-a-Velha', 1500), ('Viena', 400), ('Bruxelas', 1300),
                        ('Minsk', 1200), ('Sarajevo', 100), ('Sofia', 600), ('Zagreb', 0),
                        ('Copenhague', 1400), ('Bratislava', 600), ('Liubliana', 100), ('Madri', 1800), ('Tallinn', 1600),
                        ('Helsinque', 2000), ('Paris', 1400), ('Atenas', 900), ('Budapeste', 300), ('Roma', 400),
                        ('Pristina', 400), ('Riga', 1500), ('Vaduz', 600), ('Vilnius', 1400), ('Luxemburgo', 1200),
                        ('Skopje', 500), ('Quixinau', 900), ('Mônaco', 1000), ('Podgoricá', 300),
                        ('Oslo', 2100), ('Amsterdã', 1300), ('Varsóvia', 800), ('Lisboa', 2000),
                        ('Praga', 700), ('Bucareste', 800), ('Londres', 1700), ('Estocolmo', 1800),
                        ('Genebra', 800), ('Kiev', 1100), ('San Marino', 400)],

                  'Copenhague': [('Tirana', 1800), ('Berlim', 600), ('Andorra-a-Velha', 1800), ('Viena', 1000), ('Bruxelas', 800),
                        ('Minsk', 1200), ('Sarajevo', 1600), ('Sofia', 1900), ('Zagreb', 1400),
                        ('Copenhague', 0), ('Bratislava', 1000), ('Liubliana', 1200), ('Madri', 2200), ('Tallinn', 1000),
                        ('Helsinque', 800), ('Paris', 1200), ('Atenas', 2100), ('Budapeste', 1200), ('Roma', 1400),
                        ('Pristina', 1700), ('Riga', 900), ('Vaduz', 1200), ('Vilnius', 1000), ('Luxemburgo', 800),
                        ('Skopje', 1700), ('Quixinau', 1400), ('Mônaco', 1400), ('Podgoricá', 1600),
                        ('Oslo', 500), ('Amsterdã', 600), ('Varsóvia', 800), ('Lisboa', 2200),
                        ('Praga', 700), ('Bucareste', 1600), ('Londres', 1000), ('Estocolmo', 500),
                        ('Genebra', 1100), ('Kiev', 1500), ('San Marino', 1400)],

                  'Bratislava': [('Tirana', 900), ('Berlim', 600), ('Andorra-a-Velha', 1500), ('Viena', 300), ('Bruxelas', 1100),
                        ('Minsk', 800), ('Sarajevo', 800), ('Sofia', 1000), ('Zagreb', 600),
                        ('Copenhague', 1000), ('Bratislava', 0), ('Liubliana', 400), ('Madri', 1800), ('Tallinn', 1200),
                        ('Helsinque', 1400), ('Paris', 1300), ('Atenas', 1300), ('Budapeste', 200), ('Roma', 800),
                        ('Pristina', 800), ('Riga', 1100), ('Vaduz', 700), ('Vilnius', 900), ('Luxemburgo', 1000),
                        ('Skopje', 900), ('Quixinau', 900), ('Mônaco', 1200), ('Podgoricá', 800),
                        ('Oslo', 1600), ('Amsterdã', 1100), ('Varsóvia', 500), ('Lisboa', 2100),
                        ('Praga', 300), ('Bucareste', 700), ('Londres', 1600), ('Estocolmo', 1400),
                        ('Genebra', 900), ('Kiev', 800), ('San Marino', 800)],

                  'Liubliana': [('Tirana', 700), ('Berlim', 600), ('Andorra-a-Velha', 1200), ('Viena', 300), ('Bruxelas', 1000),
                        ('Minsk', 1300), ('Sarajevo', 300), ('Sofia', 700), ('Zagreb', 100),
                        ('Copenhague', 1200), ('Bratislava', 400), ('Liubliana', 0), ('Madri', 1600), ('Tallinn', 1500),
                        ('Helsinque', 1900), ('Paris', 1200), ('Atenas', 1000), ('Budapeste', 400), ('Roma', 400),
                        ('Pristina', 600), ('Riga', 1500), ('Vaduz', 600), ('Vilnius', 1300), ('Luxemburgo', 1000),
                        ('Skopje', 700), ('Quixinau', 1200), ('Mônaco', 1000), ('Podgoricá', 400),
                        ('Oslo', 1900), ('Amsterdã', 1200), ('Varsóvia', 900), ('Lisboa', 2200),
                        ('Praga', 500), ('Bucareste', 900), ('Londres', 1500), ('Estocolmo', 1600),
                        ('Genebra', 700), ('Kiev', 1000), ('San Marino', 300)],

                  'Madri': [('Tirana', 1900), ('Berlim', 1500), ('Andorra-a-Velha', 200), ('Viena', 1600), ('Bruxelas', 1300),
                        ('Minsk', 2500), ('Sarajevo', 1600), ('Sofia', 2300), ('Zagreb', 1800),
                        ('Copenhague', 2200), ('Bratislava', 1800), ('Liubliana', 1600), ('Madri', 0), ('Tallinn', 2600),
                        ('Helsinque', 2800), ('Paris', 900), ('Atenas', 2400), ('Budapeste', 2000), ('Roma', 1300),
                        ('Pristina', 2100), ('Riga', 2600), ('Vaduz', 1400), ('Vilnius', 2400), ('Luxemburgo', 1300),
                        ('Skopje', 2100), ('Quixinau', 2400), ('Mônaco', 1000), ('Podgoricá', 2000),
                        ('Oslo', 2900), ('Amsterdã', 1500), ('Varsóvia', 2200), ('Lisboa', 400),
                        ('Praga', 1800), ('Bucareste', 2500), ('Londres', 1400), ('Estocolmo', 2700),
                        ('Genebra', 1200), ('Kiev', 2700), ('San Marino', 1400)],

                  'Tallinn': [('Tirana', 2000), ('Berlim', 1700), ('Andorra-a-Velha', 2100), ('Viena', 1500), ('Bruxelas', 1500),
                        ('Minsk', 600), ('Sarajevo', 2000), ('Sofia', 2200), ('Zagreb', 1600),
                        ('Copenhague', 1000), ('Bratislava', 1200), ('Liubliana', 1500), ('Madri', 2600), ('Tallinn', 0),
                        ('Helsinque', 400), ('Paris', 2000), ('Atenas', 2900), ('Budapeste', 1500), ('Roma', 1700),
                        ('Pristina', 2100), ('Riga', 400), ('Vaduz', 1700), ('Vilnius', 300), ('Luxemburgo', 1600),
                        ('Skopje', 2200), ('Quixinau', 2100), ('Mônaco', 2200), ('Podgoricá', 2000),
                        ('Oslo', 500), ('Amsterdã', 1700), ('Varsóvia', 2000), ('Lisboa', 2700),
                        ('Praga', 1500), ('Bucareste', 1900), ('Londres', 2300), ('Estocolmo', 500),
                        ('Genebra', 1800), ('Kiev', 500), ('San Marino', 2200)],

                  'Helsinque': [('Tirana', 2200), ('Berlim', 2000), ('Andorra-a-Velha', 2200), ('Viena', 1900), ('Bruxelas', 1800),
                        ('Minsk', 700), ('Sarajevo', 2200), ('Sofia', 2400), ('Zagreb', 2000),
                        ('Copenhague', 800), ('Bratislava', 1400), ('Liubliana', 1900), ('Madri', 2800), ('Tallinn', 400),
                        ('Helsinque', 0), ('Paris', 2200), ('Atenas', 3000), ('Budapeste', 1700), ('Roma', 1900),
                        ('Pristina', 2300), ('Riga', 1000), ('Vaduz', 1900), ('Vilnius', 1200), ('Luxemburgo', 1700),
                        ('Skopje', 2400), ('Quixinau', 2300), ('Mônaco', 2400), ('Podgoricá', 2200),
                        ('Oslo', 900), ('Amsterdã', 2000), ('Varsóvia', 2300), ('Lisboa', 2800),
                        ('Praga', 1800), ('Bucareste', 2400), ('Londres', 2600), ('Estocolmo', 1000),
                        ('Genebra', 1900), ('Kiev', 2300), ('San Marino', 2400)],

                  'Paris': [('Tirana', 1500), ('Berlim', 1400), ('Andorra-a-Velha', 1800), ('Viena', 1300), ('Bruxelas', 300),
                        ('Minsk', 1800), ('Sarajevo', 1400), ('Sofia', 1600), ('Zagreb', 1400),
                        ('Copenhague', 1200), ('Bratislava', 1300), ('Liubliana', 1200), ('Madri', 900), ('Tallinn', 2000),
                        ('Helsinque', 2200), ('Paris', 0), ('Atenas', 2200), ('Budapeste', 1000), ('Roma', 200),
                        ('Pristina', 1600), ('Riga', 2000), ('Vaduz', 1400), ('Vilnius', 1700), ('Luxemburgo', 300),
                        ('Skopje', 1700), ('Quixinau', 1600), ('Mônaco', 1000), ('Podgoricá', 1500),
                        ('Oslo', 2300), ('Amsterdã', 300), ('Varsóvia', 1500), ('Lisboa', 900),
                        ('Praga', 1300), ('Bucareste', 1800), ('Londres', 1000), ('Estocolmo', 2200),
                        ('Genebra', 1000), ('Kiev', 1900), ('San Marino', 1400)],

                  'Atenas': [('Tirana', 800), ('Berlim', 1300), ('Andorra-a-Velha', 1600), ('Viena', 1200), ('Bruxelas', 2000),
                        ('Minsk', 2300), ('Sarajevo', 1300), ('Sofia', 400), ('Zagreb', 900),
                        ('Copenhague', 2100), ('Bratislava', 1300), ('Liubliana', 1000), ('Madri', 2400), ('Tallinn', 2900),
                        ('Helsinque', 3000), ('Paris', 2200), ('Atenas', 0), ('Budapeste', 800), ('Roma', 900),
                        ('Pristina', 1200), ('Riga', 2500), ('Vaduz', 1500), ('Vilnius', 2300), ('Luxemburgo', 2000),
                        ('Skopje', 1100), ('Quixinau', 1400), ('Mônaco', 2400), ('Podgoricá', 1300),
                        ('Oslo', 2800), ('Amsterdã', 2200), ('Varsóvia', 2400), ('Lisboa', 2900),
                        ('Praga', 2100), ('Bucareste', 700), ('Londres', 2700), ('Estocolmo', 2900),
                        ('Genebra', 2000), ('Kiev', 3000), ('San Marino', 2100)],

                  'Budapeste': [('Tirana', 500), ('Berlim', 300), ('Andorra-a-Velha', 700), ('Viena', 300), ('Bruxelas', 500),
                        ('Minsk', 1500), ('Sarajevo', 400), ('Sofia', 400), ('Zagreb', 300),
                        ('Copenhague', 1200), ('Bratislava', 200), ('Liubliana', 400), ('Madri', 2000), ('Tallinn', 1500),
                        ('Helsinque', 1700), ('Paris', 1000), ('Atenas', 800), ('Budapeste', 0), ('Roma', 600),
                        ('Pristina', 500), ('Riga', 1300), ('Vaduz', 700), ('Vilnius', 1200), ('Luxemburgo', 500),
                        ('Skopje', 1000), ('Quixinau', 1200), ('Mônaco', 1300), ('Podgoricá', 800),
                        ('Oslo', 1800), ('Amsterdã', 700), ('Varsóvia', 400), ('Lisboa', 2000),
                        ('Praga', 300), ('Bucareste', 700), ('Londres', 1400), ('Estocolmo', 1600),
                        ('Genebra', 600), ('Kiev', 1300), ('San Marino', 600)],

                  'Roma': [('Tirana', 800), ('Berlim', 400), ('Andorra-a-Velha', 1000), ('Viena', 400), ('Bruxelas', 200),
                        ('Minsk', 1800), ('Sarajevo', 400), ('Sofia', 800), ('Zagreb', 400),
                        ('Copenhague', 1400), ('Bratislava', 800), ('Liubliana', 400), ('Madri', 1300), ('Tallinn', 1700),
                        ('Helsinque', 1900), ('Paris', 200), ('Atenas', 900), ('Budapeste', 600), ('Roma', 0),
                        ('Pristina', 600), ('Riga', 1700), ('Vaduz', 800), ('Vilnius', 1500), ('Luxemburgo', 400),
                        ('Skopje', 800), ('Quixinau', 1200), ('Mônaco', 1000), ('Podgoricá', 1000),
                        ('Oslo', 1900), ('Amsterdã', 100), ('Varsóvia', 800), ('Lisboa', 1300),
                        ('Praga', 500), ('Bucareste', 800), ('Londres', 900), ('Estocolmo', 1900),
                        ('Genebra', 400), ('Kiev', 1600), ('San Marino', 400)],

                  'Pristina': [('Tirana', 200), ('Berlim', 900), ('Andorra-a-Velha', 700), ('Viena', 800), ('Bruxelas', 800),
                        ('Minsk', 2000), ('Sarajevo', 300), ('Sofia', 400), ('Zagreb', 400),
                        ('Copenhague', 1700), ('Bratislava', 800), ('Liubliana', 600), ('Madri', 2100), ('Tallinn', 2100),
                        ('Helsinque', 2300), ('Paris', 1600), ('Atenas', 1200), ('Budapeste', 500), ('Roma', 600),
                        ('Pristina', 0), ('Riga', 2200), ('Vaduz', 800), ('Vilnius', 2100), ('Luxemburgo', 800),
                        ('Skopje', 600), ('Quixinau', 700), ('Mônaco', 1000), ('Podgoricá', 300),
                        ('Oslo', 2200), ('Amsterdã', 1500), ('Varsóvia', 1200), ('Lisboa', 2300),
                        ('Praga', 800), ('Bucareste', 1600), ('Londres', 2100), ('Estocolmo', 2200),
                        ('Genebra', 700), ('Kiev', 2300), ('San Marino', 800)],

                  'Riga': [('Tirana', 1900), ('Berlim', 1300), ('Andorra la Vella', 2000), ('Viena', 1400), ('Bruxelas', 1500),
                        ('Minsk', 600), ('Sarajevo', 1700), ('Sofia', 1900), ('Zagreb', 1600), ('Copenhague', 1200),
                        ('Bratislava', 1500), ('Liubliana', 1600), ('Madri', 2300), ('Tallinn', 300), ('Helsinque', 200),
                        ('Paris', 1700), ('Atenas', 2000), ('Budapeste', 1300), ('Roma', 1600), ('Pristina', 1700),
                        ('Riga', 0), ('Vaduz', 1600), ('Vilnius', 200), ('Luxemburgo', 1600), ('Skopje', 1800),
                        ('Chisinau', 800), ('Mônaco', 1900), ('Podgorica', 1700), ('Oslo', 1500), ('Amsterdã', 1400),
                        ('Varsóvia', 900), ('Lisboa', 2300), ('Praga', 1500), ('Bucareste', 1900), ('Londres', 2100),
                        ('Estocolmo', 1200), ('Genebra', 1500), ('Kiev', 700), ('San Marino', 1900)],

                  'Vaduz': [('Tirana', 1200), ('Berlim', 200), ('Andorra la Vella', 1200), ('Viena', 100), ('Bruxelas', 700),
                        ('Minsk', 1500), ('Sarajevo', 1000), ('Sofia', 1300), ('Zagreb', 800), ('Copenhague', 1000),
                        ('Bratislava', 800), ('Liubliana', 400), ('Madri', 1400), ('Tallinn', 1700), ('Helsinque', 1800),
                        ('Paris', 600), ('Atenas', 1300), ('Budapeste', 600), ('Roma', 200), ('Pristina', 1100),
                        ('Riga', 1600), ('Vaduz', 0), ('Vilnius', 1300), ('Luxemburgo', 400), ('Skopje', 1300),
                        ('Chisinau', 1400), ('Mônaco', 600), ('Podgorica', 600), ('Oslo', 1700), ('Amsterdã', 800),
                        ('Varsóvia', 1200), ('Lisboa', 1500), ('Praga', 500), ('Bucareste', 1300), ('Londres', 1100),
                        ('Estocolmo', 1500), ('Genebra', 150), ('Kiev', 1400), ('San Marino', 900)],

                  'Vilnius': [('Tirana', 1900), ('Berlim', 1200), ('Andorra la Vella', 2000), ('Viena', 1400), ('Bruxelas', 1500),
                        ('Minsk', 400), ('Sarajevo', 1600), ('Sofia', 1600), ('Zagreb', 1400), ('Copenhague', 1300),
                        ('Bratislava', 1500), ('Liubliana', 1500), ('Madri', 2300), ('Tallinn', 100), ('Helsinque', 200),
                        ('Paris', 1700), ('Atenas', 2000), ('Budapeste', 1200), ('Roma', 1300), ('Pristina', 1800),
                        ('Riga', 200), ('Vaduz', 1300), ('Vilnius', 0), ('Luxemburgo', 1700), ('Skopje', 1700),
                        ('Chisinau', 800), ('Mônaco', 1900), ('Podgorica', 1700), ('Oslo', 1800), ('Amsterdã', 1300),
                        ('Varsóvia', 800), ('Lisboa', 2200), ('Praga', 1500), ('Bucareste', 1600), ('Londres', 2000),
                        ('Estocolmo', 1200), ('Genebra', 1300), ('Kiev', 600), ('San Marino', 2000)],

                  'Luxemburgo': [('Tirana', 1500), ('Berlim', 200), ('Andorra la Vella', 1200), ('Viena', 600), ('Bruxelas', 200),
                        ('Minsk', 1500), ('Sarajevo', 1400), ('Sofia', 1600), ('Zagreb', 1300), ('Copenhague', 900),
                        ('Bratislava', 800), ('Liubliana', 900), ('Madri', 1300), ('Tallinn', 1600), ('Helsinque', 1700),
                        ('Paris', 200), ('Atenas', 2000), ('Budapeste', 1000), ('Roma', 1200), ('Pristina', 1500),
                        ('Riga', 1600), ('Vaduz', 400), ('Vilnius', 1700), ('Luxemburgo', 0), ('Skopje', 1800),
                        ('Chisinau', 1500), ('Mônaco', 800), ('Podgorica', 1300), ('Oslo', 1700), ('Amsterdã', 400),
                        ('Varsóvia', 1200), ('Lisboa', 2000), ('Praga', 600), ('Bucareste', 1400), ('Londres', 1200),
                        ('Estocolmo', 1600), ('Genebra', 400), ('Kiev', 1400), ('San Marino', 1300)],

                  'Skopje': [('Tirana', 60), ('Berlim', 1400), ('Andorra la Vella', 1700), ('Viena', 800), ('Bruxelas', 1700),
                        ('Minsk', 1600), ('Sarajevo', 200), ('Sofia', 150), ('Zagreb', 300), ('Copenhague', 1400),
                        ('Bratislava', 1200), ('Liubliana', 500), ('Madri', 1700), ('Tallinn', 2000), ('Helsinque', 2100),
                        ('Paris', 1500), ('Atenas', 300), ('Budapeste', 700), ('Roma', 600), ('Pristina', 80),
                        ('Riga', 1800), ('Vaduz', 1200), ('Vilnius', 1700), ('Luxemburgo', 1800), ('Skopje', 0),
                        ('Chisinau', 1200), ('Mônaco', 1600), ('Podgorica', 200), ('Oslo', 1800), ('Amsterdã', 1600),
                        ('Varsóvia', 1600), ('Lisboa', 2000), ('Praga', 800), ('Bucareste', 500), ('Londres', 1700),
                        ('Estocolmo', 1800), ('Genebra', 800), ('Kiev', 600), ('San Marino', 600)],

                  'Chisinau': [('Tirana', 1300), ('Berlim', 1800), ('Andorra la Vella', 2000), ('Viena', 1300), ('Bruxelas', 2000),
                        ('Minsk', 400), ('Sarajevo', 1500), ('Sofia', 250), ('Zagreb', 1300), ('Copenhague', 1600),
                        ('Bratislava', 1300), ('Liubliana', 1400), ('Madri', 2100), ('Tallinn', 1700), ('Helsinque', 1800),
                        ('Paris', 1600), ('Atenas', 1300), ('Budapeste', 900), ('Roma', 1400), ('Pristina', 1200),
                        ('Riga', 800), ('Vaduz', 1800), ('Vilnius', 800), ('Luxemburgo', 1600), ('Skopje', 1200),
                        ('Chisinau', 0), ('Mônaco', 2000), ('Podgorica', 1300), ('Oslo', 1700), ('Amsterdã', 1700),
                        ('Varsóvia', 1400), ('Lisboa', 2200), ('Praga', 1500), ('Bucareste', 500), ('Londres', 1700),
                        ('Estocolmo', 2000), ('Genebra', 1300), ('Kiev', 600), ('San Marino', 1900)],

                  'Mônaco': [('Tirana', 1400), ('Berlim', 1500), ('Andorra la Vella', 1700), ('Viena', 100), ('Bruxelas', 1200),
                        ('Minsk', 1900), ('Sarajevo', 1500), ('Sofia', 1300), ('Zagreb', 1500), ('Copenhague', 900),
                        ('Bratislava', 1600), ('Liubliana', 1400), ('Madri', 2000), ('Tallinn', 1800), ('Helsinque', 1900),
                        ('Paris', 200), ('Atenas', 1300), ('Budapeste', 1200), ('Roma', 100), ('Pristina', 1500),
                        ('Riga', 600), ('Vaduz', 600), ('Vilnius', 1900), ('Luxemburgo', 800), ('Skopje', 1600),
                        ('Chisinau', 2000), ('Mônaco', 0), ('Podgorica', 1600), ('Oslo', 1500), ('Amsterdã', 1500),
                        ('Varsóvia', 1700), ('Lisboa', 1700), ('Praga', 800), ('Bucareste', 1700), ('Londres', 1700),
                        ('Estocolmo', 1600), ('Genebra', 200), ('Kiev', 1600), ('San Marino', 600)],

                  'Podgorica': [('Tirana', 300), ('Berlim', 1600), ('Andorra la Vella', 1800), ('Viena', 1200), ('Bruxelas', 1600),
                        ('Minsk', 1800), ('Sarajevo', 600), ('Sofia', 600), ('Zagreb', 300), ('Copenhague', 1700),
                        ('Bratislava', 1500), ('Liubliana', 700), ('Madri', 1600), ('Tallinn', 1800), ('Helsinque', 1900),
                        ('Paris', 1300), ('Atenas', 800), ('Budapeste', 1200), ('Roma', 1300), ('Pristina', 600),
                        ('Riga', 1700), ('Vaduz', 600), ('Vilnius', 1700), ('Luxemburgo', 1300), ('Skopje', 200),
                        ('Chisinau', 1300), ('Mônaco', 1600), ('Podgorica', 0), ('Oslo', 1900), ('Amsterdã', 1600),
                        ('Varsóvia', 1500), ('Lisboa', 1700), ('Praga', 1000), ('Bucareste', 600), ('Londres', 1700),
                        ('Estocolmo', 1700), ('Genebra', 1300), ('Kiev', 1000), ('San Marino', 1200)],

                  'Oslo': [('Tirana', 2000), ('Berlim', 1600), ('Andorra la Vella', 2200), ('Viena', 1700), ('Bruxelas', 1700),
                        ('Minsk', 2100), ('Sarajevo', 1800), ('Sofia', 1600), ('Zagreb', 1800), ('Copenhague', 600),
                        ('Bratislava', 1600), ('Liubliana', 1700), ('Madri', 2300), ('Tallinn', 2000), ('Helsinque', 200),
                        ('Paris', 1500), ('Atenas', 2300), ('Budapeste', 1600), ('Roma', 1700), ('Pristina', 1900),
                        ('Riga', 1500), ('Vaduz', 1700), ('Vilnius', 1800), ('Luxemburgo', 1700), ('Skopje', 1800),
                        ('Chisinau', 1700), ('Mônaco', 1500), ('Podgorica', 1900), ('Oslo', 0), ('Amsterdã', 1300),
                        ('Varsóvia', 1400), ('Lisboa', 2500), ('Praga', 1200), ('Bucareste', 1600), ('Londres', 2000),
                        ('Estocolmo', 300), ('Genebra', 1600), ('Kiev', 2200), ('San Marino', 1900)],

                  'Amsterdã': [('Tirana', 1800), ('Berlim', 600), ('Andorra la Vella', 1700), ('Viena', 800), ('Bruxelas', 100),
                        ('Minsk', 1700), ('Sarajevo', 1500), ('Sofia', 1600), ('Zagreb', 1500), ('Copenhague', 600),
                        ('Bratislava', 800), ('Liubliana', 1000), ('Madri', 1800), ('Tallinn', 1700), ('Helsinque', 1800),
                        ('Paris', 300), ('Atenas', 1800), ('Budapeste', 1000), ('Roma', 1200), ('Pristina', 1500),
                        ('Riga', 1400), ('Vaduz', 800), ('Vilnius', 1300), ('Luxemburgo', 400), ('Skopje', 1600),
                        ('Chisinau', 1700), ('Mônaco', 1500), ('Podgorica', 1600), ('Oslo', 1300), ('Amsterdã', 0),
                        ('Varsóvia', 1200), ('Lisboa', 1900), ('Praga', 500), ('Bucareste', 1300), ('Londres', 350),
                        ('Estocolmo', 1100), ('Genebra', 800), ('Kiev', 1600), ('San Marino', 1500)],

                  'Varsóvia': [('Tirana', 1700), ('Berlim', 600), ('Andorra la Vella', 1500), ('Viena', 1000), ('Bruxelas', 1200),
                        ('Minsk', 700), ('Sarajevo', 1200), ('Sofia', 1300), ('Zagreb', 1300), ('Copenhague', 1200),
                        ('Bratislava', 800), ('Liubliana', 1000), ('Madri', 1900), ('Tallinn', 1200), ('Helsinque', 1300),
                        ('Paris', 1300), ('Atenas', 1700), ('Budapeste', 600), ('Roma', 1300), ('Pristina', 1200),
                        ('Riga', 900), ('Vaduz', 1200), ('Vilnius', 800), ('Luxemburgo', 1200), ('Skopje', 1600),
                        ('Chisinau', 1400), ('Mônaco', 1700), ('Podgorica', 1500), ('Oslo', 1400), ('Amsterdã', 1200),
                        ('Varsóvia', 0), ('Lisboa', 2000), ('Praga', 500), ('Bucareste', 500), ('Londres', 1200),
                        ('Estocolmo', 1000), ('Genebra', 1200), ('Kiev', 700), ('San Marino', 1600)],

                  'Lisboa': [('Tirana', 2300), ('Berlim', 1300), ('Andorra la Vella', 1600), ('Viena', 1300), ('Bruxelas', 2000),
                        ('Minsk', 2200), ('Sarajevo', 1900), ('Sofia', 1700), ('Zagreb', 1600), ('Copenhague', 1700),
                        ('Bratislava', 1500), ('Liubliana', 1700), ('Madri', 600), ('Tallinn', 2200), ('Helsinque', 2300),
                        ('Paris', 1700), ('Atenas', 2200), ('Budapeste', 1800), ('Roma', 1700), ('Pristina', 2000),
                        ('Riga', 2300), ('Vaduz', 1500), ('Vilnius', 2200), ('Luxemburgo', 2000), ('Skopje', 2000),
                        ('Chisinau', 2200), ('Mônaco', 1700), ('Podgorica', 1700), ('Oslo', 2500), ('Amsterdã', 1900),
                        ('Varsóvia', 2000), ('Lisboa', 0), ('Praga', 1600), ('Bucareste', 1800), ('Londres', 1500),
                        ('Estocolmo', 2200), ('Genebra', 1500), ('Kiev', 2300), ('San Marino', 1700)],

                  'Praga': [('Tirana', 1600), ('Berlim', 400), ('Andorra la Vella', 1500), ('Viena', 400), ('Bruxelas', 500),
                        ('Minsk', 1500), ('Sarajevo', 700), ('Sofia', 700), ('Zagreb', 700), ('Copenhague', 500),
                        ('Bratislava', 50), ('Liubliana', 700), ('Madri', 1500), ('Tallinn', 1500), ('Helsinque', 1600),
                        ('Paris', 900), ('Atenas', 1800), ('Budapeste', 300), ('Roma', 1200), ('Pristina', 1000),
                        ('Riga', 1500), ('Vaduz', 500), ('Vilnius', 1500), ('Luxemburgo', 600), ('Skopje', 800),
                        ('Chisinau', 1500), ('Mônaco', 800), ('Podgorica', 1000), ('Oslo', 1200), ('Amsterdã', 500),
                        ('Varsóvia', 500), ('Lisboa', 1600), ('Praga', 0), ('Bucareste', 300), ('Londres', 1000),
                        ('Estocolmo', 800), ('Genebra', 500), ('Kiev', 1500), ('San Marino', 1200)],

                  'Bucareste': [('Tirana', 1900), ('Berlim', 1300), ('Andorra la Vella', 1600), ('Viena', 1200), ('Bruxelas', 1500),
                        ('Minsk', 1500), ('Sarajevo', 1200), ('Sofia', 300), ('Zagreb', 800), ('Copenhague', 1300),
                        ('Bratislava', 900), ('Liubliana', 1000), ('Madri', 1700), ('Tallinn', 1700), ('Helsinque', 1800),
                        ('Paris', 1600), ('Atenas', 500), ('Budapeste', 400), ('Roma', 1300), ('Pristina', 1100),
                        ('Riga', 1900), ('Vaduz', 1300), ('Vilnius', 1600), ('Luxemburgo', 1400), ('Skopje', 500),
                        ('Chisinau', 500), ('Mônaco', 1700), ('Podgorica', 600), ('Oslo', 1600), ('Amsterdã', 1300),
                        ('Varsóvia', 500), ('Lisboa', 1800), ('Praga', 300), ('Bucareste', 0), ('Londres', 1500),
                        ('Estocolmo', 1800), ('Genebra', 1300), ('Kiev', 800), ('San Marino', 1300)],

                  'Londres': [('Tirana', 2200), ('Berlim', 1200), ('Andorra la Vella', 1600), ('Viena', 1300), ('Bruxelas', 350),
                        ('Minsk', 1700), ('Sarajevo', 1600), ('Sofia', 1700), ('Zagreb', 1500), ('Copenhague', 1100),
                        ('Bratislava', 1200), ('Liubliana', 1300), ('Madri', 1200), ('Tallinn', 1900), ('Helsinque', 2000),
                        ('Paris', 300), ('Atenas', 2300), ('Budapeste', 1500), ('Roma', 1500), ('Pristina', 1700),
                        ('Riga', 1700), ('Vaduz', 1200), ('Vilnius', 1600), ('Luxemburgo', 350), ('Skopje', 1700),
                        ('Chisinau', 1600), ('Mônaco', 1500), ('Podgorica', 1700), ('Oslo', 2000), ('Amsterdã', 350),
                        ('Varsóvia', 1200), ('Lisboa', 1500), ('Praga', 1000), ('Bucareste', 1500), ('Londres', 0),
                        ('Estocolmo', 1600), ('Genebra', 1200), ('Kiev', 1600), ('San Marino', 1500)],

                  'Estocolmo': [('Tirana', 2200), ('Berlim', 1100), ('Andorra la Vella', 1500), ('Viena', 1300), ('Bruxelas', 1200),
                        ('Minsk', 1800), ('Sarajevo', 1600), ('Sofia', 1700), ('Zagreb', 1600), ('Copenhague', 600),
                        ('Bratislava', 1500), ('Liubliana', 1600), ('Madri', 2200), ('Tallinn', 300), ('Helsinque', 200),
                        ('Paris', 1500), ('Atenas', 2200), ('Budapeste', 1600), ('Roma', 1700), ('Pristina', 1700),
                        ('Riga', 400), ('Vaduz', 1500), ('Vilnius', 1200), ('Luxemburgo', 1600), ('Skopje', 1700),
                        ('Chisinau', 1800), ('Mônaco', 1700), ('Podgorica', 1700), ('Oslo', 300), ('Amsterdã', 1100),
                        ('Varsóvia', 1000), ('Lisboa', 2200), ('Praga', 800), ('Bucareste', 1800), ('Londres', 1600),
                        ('Estocolmo', 0), ('Genebra', 1500), ('Kiev', 1800), ('San Marino', 1700)],

                  'Genebra': [('Tirana', 2100), ('Berlim', 1000), ('Andorra la Vella', 1500), ('Viena', 800), ('Bruxelas', 400),
                        ('Minsk', 1600), ('Sarajevo', 1200), ('Sofia', 1300), ('Zagreb', 1200), ('Copenhague', 1300),
                        ('Bratislava', 900), ('Liubliana', 1100), ('Madri', 1200), ('Tallinn', 1600), ('Helsinque', 1600),
                        ('Paris', 400), ('Atenas', 2000), ('Budapeste', 1000), ('Roma', 700), ('Pristina', 1200),
                        ('Riga', 1600), ('Vaduz', 1000), ('Vilnius', 1400), ('Luxemburgo', 400), ('Skopje', 1200),
                        ('Chisinau', 1400), ('Mônaco', 1500), ('Podgorica', 1300), ('Oslo', 1600), ('Amsterdã', 800),
                        ('Varsóvia', 1200), ('Lisboa', 1500), ('Praga', 500), ('Bucareste', 1300), ('Londres', 1200),
                        ('Estocolmo', 1500), ('Genebra', 0), ('Kiev', 1500), ('San Marino', 1200)],

                  'Quieve': [('Tirana', 2200), ('Berlim', 1800), ('Andorra la Vella', 2100), ('Viena', 1800), ('Bruxelas', 1600),
                        ('Minsk', 200), ('Sarajevo', 1600), ('Sofia', 1700), ('Zagreb', 1600), ('Copenhague', 1700),
                        ('Bratislava', 1800), ('Liubliana', 1900), ('Madri', 2300), ('Tallinn', 1800), ('Helsinque', 1900),
                        ('Paris', 1600), ('Atenas', 2000), ('Budapeste', 1600), ('Roma', 1900), ('Pristina', 1000),
                        ('Riga', 1600), ('Vaduz', 1800), ('Vilnius', 200), ('Luxemburgo', 1600), ('Skopje', 1700),
                        ('Chisinau', 1000), ('Mônaco', 1900), ('Podgorica', 1000), ('Oslo', 2200), ('Amsterdã', 1600),
                        ('Varsóvia', 700), ('Lisboa', 2300), ('Praga', 1500), ('Bucareste', 800), ('Londres', 1600),
                        ('Estocolmo', 1800), ('Genebra', 1500), ('Kiev', 0), ('San Marino', 1800)],

                  'San Marino': [('Tirana', 1600), ('Berlim', 1000), ('Andorra la Vella', 1500), ('Viena', 1100), ('Bruxelas', 1200),
                        ('Minsk', 1700), ('Sarajevo', 1000), ('Sofia', 1100), ('Zagreb', 1000), ('Copenhague', 1300),
                        ('Bratislava', 1000), ('Liubliana', 1100), ('Madri', 1300), ('Tallinn', 1500), ('Helsinque', 1600),
                        ('Paris', 1200), ('Atenas', 1800), ('Budapeste', 1300), ('Roma', 100), ('Pristina', 1200),
                        ('Riga', 1500), ('Vaduz', 1200), ('Vilnius', 1400), ('Luxemburgo', 1400), ('Skopje', 1300),
                        ('Chisinau', 1500), ('Mônaco', 1000), ('Podgorica', 1200), ('Oslo', 1900), ('Amsterdã', 1500),
                        ('Varsóvia', 1600), ('Lisboa', 1700), ('Praga', 1200), ('Bucareste', 1300), ('Londres', 1500),
                        ('Estocolmo', 1700), ('Genebra', 1200), ('Kiev', 1800), ('San Marino', 0)]
                  }

  def realizaBusca(self, origem, destino):
    fronteira = []
    resultado, qtdVisitados, qtdExpandidos, arvore = self.busca(origem, destino, fronteira)
    self.mostraResultado(resultado, qtdVisitados, qtdExpandidos, arvore)
    return resultado, qtdVisitados, qtdExpandidos

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
    paises = self.rotas.get(atual.pais, [])
    for c in paises:

      if atual.pai == None or not self.ehAncestral(c[0],atual.pai):
        qtdVisitados += 1
        distancias = self.heuristicas.get(c[0], [])
        hn = 0  # Inicializa hn com um valor padrão
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

algbusca = BuscaHeuristica()
algbusca.realizaBusca('Berlim', 'Londres')