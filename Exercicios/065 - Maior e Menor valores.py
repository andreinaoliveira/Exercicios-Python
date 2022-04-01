#   Exercício Python 065 - Maior e Menor valores
#   Crie um programa que leia vários números inteiros pelo teclado.
#   No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#   O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

op = ''
soma = quant = maior = menor = 0
while op != 'N':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    while op != 'S' and op != 'N':
        op = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if op != 'S' and op != 'N':
            print("Opção inválida. Tente novamente.")

media = soma/quant
print("""
Números digitados: {}
Média dos números: {}
Maior número: {}
Menor número: {}
""".format(quant, media, maior, menor))
