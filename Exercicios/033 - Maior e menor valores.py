#   Exercício Python 033 - Maior e menor valores
#   Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

#                   Verificando o maior valor
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

#                   Verificando o menor valor
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print("O maior valor digitado foi: {}".format(maior))
print("O menor valor digitado foi: {}".format(menor))
