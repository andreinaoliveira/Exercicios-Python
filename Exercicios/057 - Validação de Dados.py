#   Exercício Python 057 - Validação de Dados
#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
if sexo == 'M':
    print("Sexo masculino registrado com sucesso")
else:
    print("Sexo feminino registrado com sucesso")
