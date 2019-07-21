#   Exercício Python 068 - Jogo do Par ou Ímpar
#   Crie um programa que leia a idade e o sexo de várias pessoas.
#   A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#       A) quantas pessoas tem mais de 18 anos.
#       B) quantos homens foram cadastrados.
#       C) quantas mulheres tem menos de 20 anos.
quantMaior = quantHomens = quantMulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        quantMaior += 1

    if sexo == 'M':
        quantHomens += 1
    elif idade < 20:
        quantMulheres += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'''
Maiores de idade cadastrados: {quantMaior}
Homens cadastrados: {quantHomens}
Mulheres com idade inferior a 20: {quantMulheres}
''')
