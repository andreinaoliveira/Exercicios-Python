#   Exercício Python 096 - Função que calcula área
#    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#    (largura e comprimento) e mostre a área do terreno.


def terreno(l, c):
    area = l * c
    print(f'A área de um terreno com {l} x {c} é de {area}m²')


print("CALCULO DA AREA DO TERRENO")
print('-'*20)

largura = float(input('Largura: (m) '))
comprimento = float(input('Comprimento: (m) '))

terreno(largura, comprimento)
