#    Exercício Python 111 - Transformando módulos em pacotes
#    Dentro do pacote que criamos no desafio 111, temos um módulo chamado dado.
#    Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
#    mas com uma validação de dados para aceitar apenas valores que seja monetários.

def leiaDinheiro(valor=''):
    while True:
        if ',' in valor or valor.isnumeric():
            a = (f'{valor}'.replace(',','.'))
            aux = float(a)
            return aux
        elif '.' in valor:
            aux = float(valor)
            return aux
        else:
            print('Valor informado inválido!')
        valor = str(input('Informe um valor: '))
