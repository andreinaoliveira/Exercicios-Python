#   Exercício Python 041 - Classificando Atletas
#   A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#   e mostre sua categoria, de acordo com a idade:
#       - Até 9 anos: MIRIM
#       - Até 14 anos: INFANTIL
#       - Até 19 anos: JÚNIOR
#       - Até 25 anos: SÊNIOR
#       - Acima de 25 anos: MASTER

from datetime import date

ano_atual = date.today().year
ano = int(input("Infome o ano de nascimento do atleta: "))
idade = ano_atual - ano

if idade <= 9:
    print("Categoria: Mirim")

elif idade <= 14:
    print("Categoria: Infantil")

elif idade <= 19:
    print("Categoria: Junior")

elif idade <= 25:
    print("Categoria: Sênior")

else:
    print("Categoria: Master")
