#   Exercício Python 098 - Função de Contador
#    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#    Seu programa tem que realizar três contagens através da função criada:
#       a) de 1 até 10, de 1 em 1
#       b) de 10 até 0, de 2 em 2
#       c) uma contagem personalizada


def contagem(i, f, p):
    print('-='*10)
    print(f'Contagem de {i} até {f} passo {p}')
    for num in range(i, f, p):
        print(num, end=' ')
    print('FIM')


contagem(1, 11, 1)
contagem(10, -1, -2)

print('Personalize a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)
