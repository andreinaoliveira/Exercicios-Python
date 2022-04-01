#   Exercício Python 049 - Tabuada v.2.0
#   Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# cores
cor = {'azul': '\033[34m',
       'lilas': '\033[35m'}

n = int(input("Informe um número para ver sua tabuada: "))
print("{}-=".format(cor['lilas'])*7)

for i in range(1, 11):
    print("{}{} x {:2} = {:3}".format(cor['azul'], n, i, n * i))
    i += 1

print("{}-=".format(cor['lilas'])*7)
