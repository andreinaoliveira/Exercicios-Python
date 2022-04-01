#   Exercício Python 010 - Conversor de Moedas
#   Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 3.85
print(("Com R${:.2f} você pode comprar ${:.2f}".format(real, dolar)))
