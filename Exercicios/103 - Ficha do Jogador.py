#   Exercício Python 103 - Ficha do Jogador
#    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#    o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
#    mesmo que algum dado não tenha sido informado

def ficha(jogador='Não informado', gols=-1):
    print('-'*40)
    print(f'{"Jogador":<20}{"Gols":<20}')
    if gols == -1:
        print(f'{jogador:<20}{"Não informado":<20}')
    else:
        print(f'{jogador:<20}{gols:<20}')

ficha()
ficha('ana')
ficha(gols=5)
ficha('marta', 3)