#   Exercício Python 088 - Palpites para a Mega Sena
#   Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#   O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo.

from random import sample
quant = int(input('Quantos jogos? '))
for i in range(1, quant+1):
    jogo = [sample(range(1, 60), 6)]
    print(f'Jogo {i}: {jogo}')
    jogo.clear()