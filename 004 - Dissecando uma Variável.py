#   Exercício Python 004 - Dissecando uma Variável
#   Faça um programa que leia algo pelo teclado
#   e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = str(input("Digite algo: "))

print("O tipo primitivo desse valor é {}".format(type(frase)))
print("Só tem espaços? {}".format(frase.isspace()))
print("É um número? {}".format(frase.isnumeric()))
print("É alfabético? {}".format(frase.isalpha()))
print("É alfanumérico? {}".format(frase.isalnum()))
print("Esta em maiúsculas? {}".format(frase.isupper()))
print("Esta em minúsculas? {}".format(frase.islower()))
print("Esta capilatizado? {}".format(frase.istitle()))
