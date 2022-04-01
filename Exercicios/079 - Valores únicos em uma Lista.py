#   Exercício Python 079 - Valores únicos em uma Lista
#   Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#   Caso o número já exista lá dentro, ele não será adicionado.
#   No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    aux = int(input('Digite um número:(-1 para sair) '))
    if aux == -1:
        break
    if aux not in numeros:
        numeros.append(aux)
    else:
        print('Número duplicado. Não irei adicionar')
numeros.sort()
print(f'Valores digitados: {numeros}')
