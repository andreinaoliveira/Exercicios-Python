#   Exercício Python 008 - Conversor de Medidas
#   Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Uma distância em metros: "))
cm = m * 100
mm = m * 1000

print("{}m corresponde a {}cm e {}mm".format(m, cm, mm))
