#   Exercício Python 018 - Seno, Cosseno e Tangente
#   Faça um programa que leia um ângulo qualquer e mostre na tela
#   o valor do seno, cosseno e tangente desse ângulo.

import math

a = float(input("Digite o ângulo que você deseja: "))
print("Seno: {:.2f}".format(math.sin(math.radians(a))))
print("Cosseno: {:.2f}".format(math.cos(math.radians(a))))
print("Tangente: {:.2f}".format(math.tan(math.radians(a))))
