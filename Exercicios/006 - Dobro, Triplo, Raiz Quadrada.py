#   Exercício Python 006 - Dobro, Triplo, Raiz Quadrada
#   Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from time import sleep

n = int(input("Digite um número: "))
print("Analisando o número {}".format(n))
sleep(1)

print("Dobro: {}".format(n*2))
print("Triplo: {}".format(n*3))
print("Raiz quadrada: {:.2f}".format(n**(1/2)))
