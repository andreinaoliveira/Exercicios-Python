#   Exercício Python 087 - Mais sobre Matriz em Python
#    Aprimore o desafio anterior, mostrando no final:
#       A) A soma de todos os valores pares digitados.
#       B) A soma dos valores da terceira coluna.
#       C) O maior valor da segunda linha.

par = terc = maior = 0
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'[{i}][{j}] = '))

        if matriz[i][j] % 2 == 0:
            par += matriz[i][j]
        if j == 2:
            terc += matriz[i][j]
        if i == 1:
            maior += matriz[i][j]

print(matriz[0])
print(matriz[1])
print(matriz[2])

print(f'''Soma dos valores digitados: {par}
Soma dos valores da terceira coluna {terc}
Maior valor da segunda linha {maior}''')
