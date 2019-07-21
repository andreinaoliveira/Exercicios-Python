#   Exercício Python 037 - Conversor de Bases Numéricas
#   Escreva um programa em Python que leia um número inteiro qualquer
#   e peça para o usuário escolher qual será a base de conversão:
#   1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Informe um número: "))
op = int(input("""1 - Binário.
2 - Octal.
3 - Hexadecimal

Converter para: """))

if op == 1:
    print("Binário: {}".format(bin(num)[2:]))
elif op == 2:
    print("Octal: {}".format(oct(num)[2:]))
elif op == 3:
    print("Hexadecimal: {}".format(hex(num)[2:]))
else:
    print("Opção Inválida.")
