#   Exercício Python 017 - Catetos e Hipotenusa
#   Faça um programa que leia o comprimento do cateto oposto
#   e do cateto adjacente de um triângulo retângulo.
#   Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
h = hypot(co, ca)
hp = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir: {:.2f}".format(h))
