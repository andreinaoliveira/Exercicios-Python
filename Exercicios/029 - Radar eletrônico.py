#   Exercício Python 029 - Radar eletrônico
#   Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#   mostre uma mensagem dizendo que ele foi multado.
#   A multa vai custar R$7,00 por cada Km acima do limite.

# cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'amarelo': '\033[33m'}

velocidade = int(input("Qual a velocidade atual do carro? "))

if velocidade < 0:
    print("Velocidade Inválida")

elif (velocidade >= 0) and (velocidade <= 80):
    print("{}Tenha um bom dia e dirija com segurança!{}".format(cor['amarelo'], cor['limpa']))

else:
    print("{}MULTADO! você excedeu o limite permitido que é 80Km/h".format(cor['vermelho']))
    print("Você deve pagar uma multa de {}R${:.2f}!{}".format(cor['amarelo'], (velocidade-80)*7, cor['limpa']))
