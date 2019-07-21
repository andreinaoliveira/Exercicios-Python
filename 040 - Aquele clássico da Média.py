#   Exercício Python 040 - Aquele clássico da Média
#   Crie um programa que leia duas notas de um aluno e calcule sua média,
#   mostrando uma mensagem no final, de acordo com a média atingida:
#       - Média abaixo de 5.0: REPROVADO
#       - Média entre 5.0 e 6.9: RECUPERAÇÃO
#       - Média 7.0 ou superior: APROVADO

n1 = float(input("Informa a primeira nota: "))
n2 = float(input("Informa a segunda nota: "))

media = (n1 + n2) / 2

print("A média do aluno é {:.1f}".format(media))
if 7 > media >= 5:
    print("Recuperação")
elif media < 5:
    print("Reprovado")
elif media >= 7:
    print("Aprovado")
