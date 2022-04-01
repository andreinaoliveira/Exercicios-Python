#   Exercício Python 099 - Função que descobre o maior
#    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*num):
    print(f'Valores recebidos {num}')
    print(f'Maior valor: {max(num)}')


maior(1, 2, 3, 9, 5)
