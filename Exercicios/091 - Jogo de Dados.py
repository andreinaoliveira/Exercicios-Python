#   Exercício Python 091 - Jogo de Dados em Python
#   Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#   Guarde esses resultados em um dicionário em Python.
#   No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, j in jogo.items():
    print(f'{i} tirou {j}')

for i, j in enumerate(ranking):
    print(f'{i+1} lugar: {j[0]} com {j[1]}')
