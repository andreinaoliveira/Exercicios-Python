#   Exercício Python 084 - Lista composta e análise de dados
#   Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas.
#       B) Uma listagem com as pessoas mais pesadas.
#       C) Uma listagem com as pessoas mais leves.

aux = []
pessoas = []
maior = menor = 0

while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]

        if aux[1] < menor:
            menor = aux[1]

    pessoas.append(aux[:])
    aux.clear()

    op = str(input('Continuar? [S/N]')).strip().upper()
    if op == 'N':
        break

print(f'''Quantidade: {len(pessoas)}
Maior Peso {maior}
Menor Peso: {menor}''')
