#   Exercício Python 039 - Alistamento Militar
#   Faça um programa que leia o ano de nascimento de um jovem
#   e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#   se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano = int(input("Infome seu ano de nascimento: "))

idade = ano_atual - ano

print("Quem naceu em {} tem {} anos no ano de {}.".format(ano, idade, ano_atual))

if idade < 18:
    print("VocÊ irá se alistar em {} ano(s)".format(18 - idade))
    print("Você deverá se alistar em {} ".format(ano_atual + (18-idade)))

elif idade == 18:
    print("Você irá se alistar nesse ano de {}".format(ano_atual))

elif idade > 18:
    print("Você deveria ter se alistado há {} anos".format(idade-18))
    print("Seu alistamento foi em {}".format(ano_atual - (idade - 18)))
