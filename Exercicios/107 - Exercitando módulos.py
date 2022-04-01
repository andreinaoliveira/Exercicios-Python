#    Exercício Python 107 - Exercitando módulos em Python
#    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#    Faça também um programa que importe esse módulo e use algumas dessas funções.

from pacote import moeda

num = float(input('Informe um valor: '))
print(f'''Aumento de 10%: R${moeda.aumentar(num, 10):.2f}
Subtração de 10%: R${moeda.diminuir(num, 10):.2f}
Dobro: R${moeda.dobro(num):.2f}
Metade: R${moeda.metade(num):.2f}''')
