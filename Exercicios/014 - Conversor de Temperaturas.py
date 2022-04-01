#   Exercício Python 014 - Conversor de Temperaturas
#   Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Informe a temperatura em ºC: "))
f = (9 * c / 5)+32

print("A temperatura de {:.1f}ºC corresponte a {:.1f}ºF".format(c, f))
