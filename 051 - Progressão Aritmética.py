#   Exercício Python 051 - Progressão Aritmética
#   Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#   No final, mostre os 10 primeiros termos dessa progressão.

print("="*20)
print("PROGRESSÃO DE UMA PA")
print("="*20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + 10 * razao

for i in range(termo, decimo, razao):
    print(i, end=' -> ')
print("FIM")
