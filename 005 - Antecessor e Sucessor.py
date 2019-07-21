#   Exercício Python 005 - Antecessor e Sucessor
#   Faça um programa que leia um número Inteiro
#   e mostre na tela o seu sucessor e seu antecessor.

from time import sleep

n = int(input("Digite um número: "))
print("Analisando o número {}...".format(n))
sleep(1)
print("Antecessor: {}".format(n-1))
print("Sucessor: {}".format(n+1))
