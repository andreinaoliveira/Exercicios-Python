#   Exercício Python 099 - Função que descobre o maior
#    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#    A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
#    a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Lista: {lista}')


def soma(lista):
    print(f'A soma entre os itens da lista é: {sum(lista)}')


numeros = list()
sorteia(numeros)
soma(numeros)
