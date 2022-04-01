#   Exercício Python 013 - Reajuste Salarial
#   Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input("Qual o salário do funcionário? R$"))
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(s, s+(s * 15 / 100)))
