#   Exercício Python 055 - Maior e menor da sequência
#   Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000
for i in range(1, 6):
    peso = float(input("Informe o peso da {}º pessoa: ".format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("""
Maior peso: {}
Menor peso {}
""".format(maior, menor))
