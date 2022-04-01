#   Exercício Python 094 - Unindo dicionários e listas
#   Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas
#       B) A média de idade
#       C) Uma lista com as mulheres
#       D) Uma lista de pessoas com idade acima da média

lista = list()
mulheres = list()
dicionario = dict()
soma = 0

while True:
    dicionario.clear()
    dicionario['Nome'] = str(input('Nome: ')).strip()
    dicionario['Idade'] = int(input('Idade: '))

    while True:
        dicionario['Sexo:'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if dicionario['Sexo:'] in 'MF':
            break
        print('Opção Inválida! Tente novamente, desta vez com M ou F.')

    lista.append(dicionario.copy())
    soma += dicionario['Idade']

    if dicionario['Sexo:'] == 'F':
        mulheres.append(dicionario['Nome'])

    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
    if op == 'N':
        break


print(f'''A) Total de pessoas cadastradas: {len(lista)}
B) Média de idade: {soma/len(lista):.2f}
C) Mulheres cadastradas {mulheres}
D) Pessoas com idade acima da média: ''')

for a in lista:
    if a['Idade'] >= soma/len(lista):
        print(f'     {a["Nome"]}: {a["Idade"]}')
