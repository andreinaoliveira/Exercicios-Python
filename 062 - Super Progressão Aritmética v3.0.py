#   Exercício Python 062 - Super Progressão Aritmética v3.0
#   Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#   Oprograma encerrará quando ele disser que quer mostrar 0 termos.

print("="*20)
print("PROGRESSÃO DE UMA PA")
print("="*20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

contador = 0
total = 10
mais = 0
while contador < total:
    while contador < total:
        print("{}".format(termo), end=' -> ')
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais você quer? "))
    if mais == 0:
        contador = total
    total += mais
print("Progressão finalizada com o total de {} termos".format(total))
