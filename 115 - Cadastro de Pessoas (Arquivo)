import pessoas
import os

layout = {'limpar': '\033[m',
          'azul': '\033[36m',
          'amarelo': '\033[33m',
          'vermelho': '\033[31m',
          'barra': '----------------------------------------'}

while True:
    print(layout['azul'])
    print(layout['barra'])
    print('SISTEMA DE CADASTRO DE PESSOAS'.center(40))
    print(layout['barra'])
    print('''     1 - NOVO CADASTRO\n     2 - PESSOAS CADASTRADAS\n     0 - SAIR''')

    op = int(input(f'''{layout['azul']}Opção desejada: '''))

    print(layout['limpar'])

    if op == 1:
        print(layout['amarelo'])
        print(layout['barra'])
        print('NOVO CADASTRO'.center(40))
        print(layout['barra'])

        nome = input('Informe o Nome: ')
        idade = int(input('Informe a idade: '))

        print(layout['barra'])
        print(layout['limpar'])
        pessoas.cadastrarPessoa(nome, idade)

    elif op == 2:
        print(layout['amarelo'])
        print(layout['barra'])
        print('PESSOAS CADASTRADAS'.center(40))
        print(layout['barra'])
        pessoas.imprimir()
        print(layout['barra'], layout['limpar'])
        os.system("PAUSE")

    elif op == 0:
        print(layout['amarelo'])
        print('Volte Sempre!')
        print(layout['limpar'])
        break

    else:
        print(layout['vermelho'])
        print('Opção inválida!')
        print(layout['limpar'])
        os.system("PAUSE")
