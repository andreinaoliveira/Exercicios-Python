#   Exercício Python 044 - Gerenciador de Pagamentos
#   Elabore um programa que calcule o valor a ser pago por um produto,
#   considerando o seu preço normal e condição de pagamento:
#       - à vista dinheiro/cheque: 10% de desconto
#       - à vista no cartão: 5% de desconto
#       - em até 2x no cartão: preço formal
#       - 3x ou mais no cartão: 20% de juros
preco = float(input("Informe o valor do produto: R$"))
print("""1 - À vista (dinheiro ou cheque)
2 - À vista (cartão)
3 - 2x no cartão
4 - 3x ou mais""")

op = int(input("Informe a codição de pagamento: "))

if op == 1:
    print("O valor do produto será R${:.2f} com a aplicação de 10% de desconto".format(preco - (preco*10)/100))

elif op == 2:
    print("O valor do produto será R${:.2f} com a aplicação de 5% de desconto".format(preco - (preco * 5) / 100))

elif op == 3:
    print("O valor do produto será R${:.2f}".format(preco))
    print("A parcela será de 2x de R${:.2f}".format(preco / 2))

elif op == 4:
    quantidade = int(input("Quantas parcelas? "))
    parcela = (preco + (preco * 20) / 100) / quantidade
    print("O valor do produto será R${:.2f} com a aplicação de 20% de juros".format(preco + (preco * 20) / 100))
    print("A parcela será de {}x de R${:.2f}".format(quantidade, parcela))

else:
    print("Opção de Pagamento inválida")
