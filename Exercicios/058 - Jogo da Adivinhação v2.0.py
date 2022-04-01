#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#   Só que agora o jogador vai tentar adivinhar até acertar, #   mostrando no final
#   quantos palpites foram necessários para vencer.

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
print("{}Vou pensar em um número entre 1 e 10. Tente adivinhar...{}".format(cor['azul'], cor['limpa']))
print("{}-=-{}".format(cor['amarelo'], cor['limpa']) * 19)

computador = randint(1, 10)

jogador = -1
tentativas = 0
while jogador != computador:
    jogador = int(input("Em que número eu pensei? "))
    tentativas += 1

    print("{}Processando...{}".format(cor['lilas'], cor['limpa']))
    sleep(2)

    if jogador > computador:
        print("{}Que pena, você errou. Tente um número menor.{}".format(cor['vermelho'], cor['limpa']))
    else:
        print("{}Que pena, você errou. Tente um número maior.{}".format(cor['vermelho'], cor['limpa']))
print("{}PARABPENS! Você acertou com o total de {} tetativa(s){}".format(cor['verde'], tentativas, cor['limpa']))
