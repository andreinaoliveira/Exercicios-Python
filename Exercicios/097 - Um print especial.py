#   Exercício Python 097 - Um print especial
#    Faça um programa que tenha uma função chamada escreva(),
#    que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(msg):
    len(msg)
    print('~'*len(msg))
    print(msg)
    print('~' * len(msg))


txt = str(input('Diga uma mensagem: '))
escreva(txt)
