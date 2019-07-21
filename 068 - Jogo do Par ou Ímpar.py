#   Exercício Python 068 - Jogo do Par ou Ímpar
#   Faça um programa que jogue par ou ímpar com o computador.
#   O jogo só será interrompido quando o jogador perder,
#   mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
c = 0
while True:
    valor = int(input('Diga um valor: '))
    vcomputador = randint(0, 10)
    jogador = 'y'

    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    soma = valor + vcomputador
    print(f'Você jogou {valor} e o computador {vcomputador}. Total de {soma} é ', end='')

    if jogador == 'P':
        if soma % 2 == 0:
            print('PAR.')
            print('Você ganhou!')
            c += 1
        else:
            print('IMPAR.')
            print('Você Perdeu!')
            break
    else:
        if soma % 2 == 0:
            print('PAR.')
            print('Você Perdeu!')
            break
        else:
            print('IMPAR.')
            print('Você Ganhou!')
            c += 1
print(f'Game Over! Você venceu {c} vezes.')
