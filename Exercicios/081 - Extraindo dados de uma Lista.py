#   Exercício Python 081 - Extraindo dados de uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#       A) Quantos números foram digitados.
#       B) A lista de valores, ordenada de forma decrescente.
#       C) Se o valor 5 foi digitado e está ou não na lista.

n = list()
c = -1
while True:
    c += 1
    n.append(int(input('Difite um número: (0 para sair) ')))
    if n[c] == 0:
        n.pop()
        c -= 1
        break
n.sort(reverse=True)
print(f'''Números digitados: {c+1}
Valores em ordem decrescente: {n}
Valor 5 foi digitado? {'Sim' if 5 in n else 'Não'}''')
