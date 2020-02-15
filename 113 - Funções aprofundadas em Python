#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaINT():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido\033[m')
        else:
            return n


def leiaFLOAT():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número real válido\033[m')
        else:
            return n


num1 = leiaINT()
num2 = leiaFLOAT()

print('-'*20)
print(f'''Número Inteiro: {num1}
Número real: {num2}''')
print('-'*20)
