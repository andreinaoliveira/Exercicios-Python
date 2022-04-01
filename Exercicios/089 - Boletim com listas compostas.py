#   Exercício Python 089 - Boletim com listas compostas
#   Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
#   as notas de cada aluno individualmente.

boletim = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('1º Nota: '))
    n2 = float(input('2º Nota: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    op = str(input('Continuar? [S/N]')).strip().upper()
    if op == 'N':
        break

print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>5}')
print('-'*25)
for i, v in enumerate(boletim):
    print(f'{i:<5}{v[0]:<10}{v[2]:>8}')
print('-'*25)

while True:
    ref = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if ref == 999:
        break
    print(f'Notas do(a) {boletim[ref][0]} são: {boletim[ref][1]}')
