#   Exercício Python 074 - Maior e menor valores em Tupla
#   Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#   Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

num = tuple(sample(range(10), 5))
for i in num:
    print(i, end=' ')
print(f'''
Maior valor sorteado: {max(num)}
Menor valor sorteado: {min(num)}.''')
