#   Exercício Python 073 - Tuplas com Times de Futebol
#   Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#   na ordem de colocação. Depois mostre:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA', 'Avaí')

op = int(input('''
[ 1 ] Imprimir os 5 primeiros colocados.
[ 2 ] Imprimir os 4 ultimos colocados.
[ 3 ] Imprimir Classificação dos times.
[ 4 ] Imprimir os times em ordem alfabética.
[ 5 ] Posição do time chapecoence.
Sua Opção: '''))

if op == 1:
    for time in range(0, 5):
        print(f'{time+1}º {times[time]}')
elif op == 2:
    for time in range(16, 20):
        print(f'{time + 1}º {times[time]}')
elif op == 3:
    for time in range(0, 20):
        print(f'{time + 1}º {times[time]}')
elif op == 4:
    print(f'Times em ordem alfabética: {sorted(times)}')
elif op == 5:
    print(f'Chapecoence está na {times.index("Chapecoence")+1} posição.')
else:
    print('Opção Inválida.')
