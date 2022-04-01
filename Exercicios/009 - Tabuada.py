#   Exercício Python 009 - Tabuada
#   Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

# cores
cor = {'azul': '\033[34m',
       'lilas': '\033[35m'}

n = int(input("Informe um número para ver sua tabuada: "))
print("{}-=".format(cor['lilas'])*7)

i = 1
while i <= 10:
    print("{}{} x {:2} = {:3}".format(cor['azul'], n, i, n * i))
    i = i + 1

print("{}-=".format(cor['lilas'])*7)
