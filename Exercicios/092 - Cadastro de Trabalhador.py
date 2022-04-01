#   Exercício Python 089 - Boletim com listas compostas
#   Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.

from datetime import datetime

Trabalhador = dict()
while True:
    Trabalhador['Nome'] = str(input('Nome: ')).strip()
    nascimento = int(input('Ano de Nascimento: '))
    Trabalhador['Idade'] = datetime.now().year - nascimento
    Trabalhador['CTPS'] = int(input('Carteira de Trabalho: (0 não tem) '))

    if Trabalhador['CTPS'] == 0:
        Trabalhador['CTPS'] = "Não possui"
        break
    else:
        Trabalhador['Contratação'] = int(input('Ano de Contratação: '))
        Trabalhador['Salário'] = float(input('Salário: R$'))
        Trabalhador['Aposentadoria'] = (Trabalhador['Contratação'] - nascimento) + 35
    break

print('-'*20)
for i, j in Trabalhador.items():
    print(f'{i}: {j}')
