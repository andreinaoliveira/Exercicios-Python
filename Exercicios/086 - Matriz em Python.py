#   Exercício Python 086 - Matriz em Python
#   Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#   No final, mostre a matriz na tela, com a formatação correta.

matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'[{i}][{j}] = '))

print(matriz[0])
print(matriz[1])
print(matriz[2])
