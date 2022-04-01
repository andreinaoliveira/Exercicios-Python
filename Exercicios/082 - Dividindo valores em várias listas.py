#   Exercício Python 079 - Valores únicos em uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista.
#   Depois disso, crie duas listas extras que vão conter apenas os valores pares e
#   os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: (0 para sair) ')))
    if lista[-1] == 0:
        lista.pop()
        break

    if lista[-1] % 2 == 0:
        par.append(lista[-1])
    else:
        impar.append(lista[-1])

print(f'''Lista: {lista}
Par: {par}
Impar: {impar}''')
