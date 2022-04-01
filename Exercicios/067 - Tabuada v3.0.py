#   Exercício Python 067 - Tabuada v3.0
#   Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#   O programa será interrompido quando o número solicitado for negativo.

# cores
cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}
while True:
    n = int(input("Informe um número para ver sua tabuada: "))
    if n < 0:
        break
    print("{}-={}".format(cor['lilas'], cor['limpa'])*7)

    for i in range(1, 11):
        print("{}{} x {:2} = {:3}".format(cor['azul'], n, i, n * i))
        i += 1

    print("{}-={}".format(cor['lilas'], cor['limpa'])*7)
print("Programa Encerrado.")
