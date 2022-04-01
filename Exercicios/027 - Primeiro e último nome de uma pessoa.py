#   Exercício Python 027 - Primeiro e último nome de uma pessoa
#   Faça um programa que leia o nome completo de uma pessoa
#   moastrando em seguido o primeiro e ultimo nome separadamente.

nome = str(input("Informe seu nome completo: ")).strip()

n = nome.split()
print("Seu primeiro nome é {}.".format(n[0]))
print("Seu sobrenome é: {}.".format(n[len(n)-1]))
