#   Exercício Python 090 - Dicionário
#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.

aluno = {'Nome': str(input('Nome: ')).strip(),
         'Média': float(input('Média: '))}

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
else:
    aluno['Situação'] = 'Reprovado(a)'

for i, j in aluno.items():
    print(f'{i}: {j}')
