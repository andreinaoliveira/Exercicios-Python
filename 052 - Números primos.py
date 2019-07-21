#   Exercício Python 052 - Números primos
#   Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
total = 0
num = int(input("Digite um número: "))
for i in range(1, num + 1):
    if num % i == 0:
        total += 1
print("O número {} {}".format(num, "é primo" if total > 2 else "não é primo"))
