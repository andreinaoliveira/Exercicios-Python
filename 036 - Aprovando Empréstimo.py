#   Exercício Python 036 - Aprovando Empréstimo
#   Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#   Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#   A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Informe o valor do imóvel: "))
salario = float(input("Informe sua renda mensal: "))
anos = int(input("Informe em quantos anos de financiamento: "))

prestacao = casa / (anos * 12)

if prestacao > (salario*30/100):
    print("Infelizmente, o empréstimo foi negado pois a porestação é superior a 30% de sua renda mensal.")
else:
    print("Empréstimo aceito. A prestação será de R${:.2f}. Para pagemtno em {} meses.".format(prestacao, anos * 12))
