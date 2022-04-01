#   Exercício Python 028 - Jogo da Adivinhação v.1.0
#   Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#   e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#   O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

# cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

print("{}-=-{}".format(cor['amarelo'], cor['limpa']) * 19)
print("{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}".format(cor['azul'], cor['limpa']))
print("{}-=-{}".format(cor['amarelo'], cor['limpa']) * 19)

computador = randint(0, 5)
jogador = int(input("Em que número eu pensei? "))

print("{}Processando...{}".format(cor['lilas'], cor['limpa']))
sleep(3)

if jogador == computador:
    print("{}PARABPENS! Você acertou!{}".format(cor['verde'], cor['limpa']))
else:
    print("{}Que pena, você errou. Pensei no número {}{}".format(cor['vermelho'], computador, cor['limpa']))
