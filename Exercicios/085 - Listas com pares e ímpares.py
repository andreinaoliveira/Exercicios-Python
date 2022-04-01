#   Exercício Python 085 - Listas com pares e ímpares
#   Crie um programa onde o usuário possa digitar sete valores numéricos e
#   cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#   No final, mostre os valores pares e ímpares em ordem crescente.
valor = [[], []]
for i in range(1, 8):
    aux = int(input(f'Digite o {i}º Número: '))
    if aux % 2 == 0:
        valor[0].append(aux)
    else:
        valor[1].append(aux)
valor[0].sort()
valor[1].sort()
print(f'''Pares {valor[0]}
Impares {valor[1]}''')
