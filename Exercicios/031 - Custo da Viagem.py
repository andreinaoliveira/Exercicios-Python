#   Exercício Python 031 - Custo da Viagem
#   Desenvolva um programa que pergunte a distância de uma viagem em Km.
#   Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
#   200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Qual a distância da sua viagem? "))

print("Você está prestes a começar uma viage de {:.1f}Km.".format(distancia))
print("E o preço da sua viagem será de R${:.2f}".format(distancia*0.5 if distancia <= 200 else distancia*0.45))
