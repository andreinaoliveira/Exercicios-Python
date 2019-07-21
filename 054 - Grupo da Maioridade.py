#   Exercício Python 054 - Grupo da Maioridade
#   Crie um programa que leia o ano de nascimento de sete pessoas.
#   No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
maior = menor = 0
for i in range(1, 8):
    ano = int(input("Em que ano a {}º pessoa nasceu? ".format(i)))
    if ano_atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print("""
Maiores de idade: {}
Menores de idade: {}
""".format(maior, menor))
