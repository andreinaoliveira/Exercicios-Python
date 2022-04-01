#   Exercício Python 023 - Separando dígitos de um número
#   Faça um programa que leia um número de 0 a 9999
#   e mostre na tela cada um dos dígitos separados.


num = int(input("Informe um número entre 0 a 9999: "))
print("Analisando o número {}".format(num))

n = str(num)

if (num >= 0) and (num <= 9):
    print("Unidade {}".format(n[0]))

elif (num >= 10) and (num <= 99):
    print("Unidade {}".format(n[1]))
    print("Dezena {}".format(n[0]))

elif (num >= 100) and (num <= 199):
    print("Unidade {}".format(n[2]))
    print("Dezena {}".format(n[1]))
    print("Centena {}".format(n[0]))

elif (num >= 1000) and (num <= 1999):
    print("Unidade {}".format(n[3]))
    print("Dezena {}".format(n[2]))
    print("Centena {}".format(n[1]))
    print("Milhar {}".format(n[0]))

else:
    print("Número fora do requisito")
