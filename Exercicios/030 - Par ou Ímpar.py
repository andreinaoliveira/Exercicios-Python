#   Exercício Python 030 - Par ou Ímpar?
#   Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# cores
cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

numero = int(input("{}Me diga um número qualquer: ".format(cor['lilas'])))
print("O número {} é {}{}".format(numero, cor['azul'], 'PAR'if numero % 2 == 0 else 'ÍMPAR'))
