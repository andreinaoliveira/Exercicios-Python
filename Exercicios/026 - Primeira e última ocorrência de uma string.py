#   Exercício Python 026 - Primeira e última ocorrência de uma string
#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez


nome = str(input("Informe seu nome: ")).upper().strip()
print("A letra 'A' aparece {} vezes".format(nome.count('A')))
print("A primeira vez aparece na {} posição".format(nome.find('A')+1))
print("A última vez aparece na {} posição".format(nome.rfind('A')))
