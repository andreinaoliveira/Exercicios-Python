#   Exercício Python 070 - Estatísticas em produtos
# #   Crie um programa que leia o nome e o preço de vários produtos.
# #   O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# #       A) qual é o total gasto na compra.
# #       B) quantos produtos custam mais de R$1000.
# #       C) qual é o nome do produto mais barato.

maiorMil = totalGasto = c = barato = 0
nbarato = ' '
while True:
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$'))

    totalGasto += preco
    c += 1
    if c == 1:
        barato = preco

    if preco >= 1000:
        maiorMil += 1

    if barato > preco:
        barato = preco
        nbarato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break
print(f'''
Total Gasto na compra: R${totalGasto:.2f}
Qunatidade de produtos superior a R$1.000: {maiorMil}
O produto mais barato é {nbarato} que custa R${barato:.2f}
''')
