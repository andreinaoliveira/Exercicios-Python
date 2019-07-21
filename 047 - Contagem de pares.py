#   Exercício Python 047 - Contagem de pares
#   Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=', ')
print("Fim")
