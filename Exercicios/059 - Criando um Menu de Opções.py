#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Crie um programa que leia dois valores e mostre um menu na tela:
#       [ 1 ] somar
#       [ 2 ] multiplicar
#       [ 3 ] maior
#       [ 4 ] novos números
#       [ 5 ] sair do programa
#   Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Priveiro Valor: "))
n2 = int(input("Segundo Valor: "))
op = 0
while op != 5:
    print("=-"*15)
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    print("=-" * 15)
    op = int(input(">>>> Opção desejada: "))
    if op == 1:
        print("Resultado: {} + {} = {}".format(n1, n2, n1+n2))
    elif op == 2:
        print("Resultado: {} x {} = {}".format(n1, n2, n1*n2))
    elif op == 3:
        print("Resultado: Entre {} e {}, o maior número é {}".format(n1, n2, n1 if n1 > n2 else n2))
    elif op == 4:
        n1 = int(input("Priveiro Valor: "))
        n2 = int(input("Segundo Valor: "))
    elif op < 1 or op > 5:
        print("Opção inválida. Tente Novamente")
