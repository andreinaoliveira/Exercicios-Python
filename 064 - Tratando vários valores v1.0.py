#   Exercício Python 061 - Progressão Aritmética v2.0
#   Crie um programa que leia vários números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#   No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = soma = 0
c = -1
while n != 999:
    soma += n
    c += 1
    n = int(input("Digite um numero: "))
print("Foram digitados {} números e a soma entre eles é {}".format(c, soma))
