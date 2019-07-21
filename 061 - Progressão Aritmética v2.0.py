#   Exercício Python 061 - Progressão Aritmética v2.0
#   Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#   mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("="*20)
print("PROGRESSÃO DE UMA PA")
print("="*20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
c = 1
while c < 11:
    print("{}".format(termo), end=' -> ')
    termo += razao
    c += 1
print("FIM")
