#   Exercício Python 093 - Cadastro de Jogador de Futebol
#   Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#   O programa vai ler o nome do jogador e quantas partidas ele jogou.
#   Depois vai ler a quantidade de gols feitos em cada partida.
#   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

gols = list()
jogador = dict()

jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? '))

if partidas > 0:
    for c in range(0, partidas):
        gols.append(int(input(f'     Quantos gols na {c+1}º partida? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)

print('-='*40)
print(jogador)

print('-='*40)
for i, j in jogador.items():
    print(f'{i}: {j}')

print('-='*40)
print(f'O(a) jogador(a) {jogador["Nome"]} jogou {partidas} partidas')
for i, j in enumerate(gols):
    print(f'     Na {i+1}º partida fez {j} gol(s)')
print(f'Foi um total de {jogador["Total"]} gol(s)')
