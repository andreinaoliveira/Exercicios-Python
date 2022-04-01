#   Exercício Python 080 - Lista ordenada sem repetições
#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#   já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = list()
for c in range(0, 5):
    aux = int(input('Digite um número: '))
    if c == 0 or aux > numeros[-1]:
        numeros.append(aux)
        print(f'O valor {aux} foi adicionado na última posição')
    else:
        p = 0
        while p < len(numeros):
            if aux <= numeros[p]:
                numeros.insert(p, aux)
                print(f'O valor {aux} foi adicionado na posição {p}')
                break
            p += 1

print(f'Valores digitados: {numeros}')
