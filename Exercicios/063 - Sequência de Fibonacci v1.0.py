#   Exercício Python 061 - Progressão Aritmética v2.0
#   Escreva um programa que leia um número N inteiro qualquer e mostre na tela
#   os N primeiros elementos de uma Sequência de Fibonacci.

N = int(input("Quantos termos você quer mostrar? "))
c = j = 0
i = 1

while c < N:
    k = i + j
    print(j, end=' -> ')
    j = i
    i = k
    c += 1
print("FIM")
