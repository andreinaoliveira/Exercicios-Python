#   Exercício Python 104 - Validando entrada de dados em Python
#    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
#    só que fazendo a validação para aceitar apenas um valor numérico.


def leiaInt(n):
    while not n.isnumeric():
        print(f'{n} não é um número')
        n = input('Digite um número: ')
    return n


aux = leiaInt(input('Digite um número: '))
print(f'Você digitou o número {aux}')
