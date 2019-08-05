#    Exercício Python 109 - Formatando Moedas
#    Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#    informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from pacote import moeda

num = float(input('Informe um valor: '))
print(f'''Aumento de 10%: {moeda.aumentar(num, 10, formatacao=True)}
Subtração de 10%: {moeda.diminuir(num, 10, formatacao=True)}
Dobro: {moeda.dobro(num, formatacao=True)}
Metade: {moeda.metade(num, formatacao=True)}''')
