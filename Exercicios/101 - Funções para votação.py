#   Exercício Python 101 - Funções para votação
#    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
#    pessoa retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return 'Voto: Negado'
    elif idade >= 18:
        return 'Voto: Obrigatório'
    else:
        return 'Voto: Opcional'


nascimento = int(input('Informe a data de nascimento: '))
print(voto(nascimento))
