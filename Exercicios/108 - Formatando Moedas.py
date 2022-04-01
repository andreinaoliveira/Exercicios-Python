#    Exercício Python 108 - Formatando Moedas
#    Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
#    números como um valor monetário formatado.

from pacote import moeda

num = float(input('Informe um valor: '))
print(f'''Aumento de 10%: {moeda.moeda(moeda.aumentar(num, 10))}
Subtração de 10%: {moeda.moeda(moeda.diminuir(num, 10))}
Dobro: {moeda.moeda(moeda.dobro(num))}
Metade: {moeda.moeda(moeda.metade(num))}''')
