#   Exercício Python 035 - Analisando Triângulo v1.0
#   Desenvolva um programa que leia o comprimento de três retas
#   e diga ao usuário se elas podem ou não formar um triângulo.

print("-=" * 12)
print("Analisador de Triângulos")
print("-=" * 12)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Teceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar triângulo")
else:
    print("Os segmentos acima não podem formar triângulo")
