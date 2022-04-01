#    Exercício Python 107 - Exercitando módulos em Python
#    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#    Faça também um programa que importe esse módulo e use algumas dessas funções.


def moeda(preco, moeda='R$'):
    """
    Retorna o preço formatado para moeda
    :param preco: Valor do produto
    :param moeda: A moeda desejada para a formatação, por padrão, real
    :return: Preco formatado para moeda
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(preco, taxa, formatacao=False):
    """
    Função para aumentar uma porcentagem sobre o produto
    :param preco: Preço do produto
    :param taxa: Porcentagem que será somada no produto
    :param formatacao: Se True retorna o preço formatado com a função moeda()
    :return: Aumento de taxa
    """

    novoPreco = preco + (preco * taxa / 100)
    return novoPreco if formatacao is False else moeda(novoPreco)


def diminuir(preco, taxa, formatacao=False):
    """
    Função para diminuir uma porcentagem sobre o produto
    :param preco: Preço do produto
    :param taxa: Porcentagem que será somada no produto
    :param formatacao: Se True retorna o preço formatado com a função moeda()
    :return: Desconto de taxa
    """

    novoPreco = preco - (preco * taxa / 100)
    return novoPreco if formatacao is False else moeda(novoPreco)


def dobro(preco, formatacao=False):
    """
    Função para calcular o dobro do preço
    :param preco: Preço do produto
    :param formatacao: Se True retorna o preço formatado com a função moeda()
    :return: Dobro do produto
    """

    novoPreco = preco * 2
    return novoPreco if formatacao is False else moeda(novoPreco)


def metade(preco, formatacao=False):
    """
    Função para calcular a metade do preço
    :param preco: Preço do produto
    :param formatacao: Se True retorna o preço formatado com a função moeda()
    :return: Metade do preço
    """

    novoPreco = preco / 2
    return novoPreco if formatacao is False else moeda(novoPreco)


def resumo(preco, aumento, desconto):
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'''{"Preço Analisado: ":<20}{moeda(preco):>10}
{"Dobro do preço: ":<20}{dobro(preco, formatacao=True):>10}
{"Metade do preço: ":<20}{metade(preco, formatacao=True):>10}
{aumento}{"% de aumento: ":<18}{aumentar(preco, aumento, formatacao=True):>10}
{desconto}{"% de desconto: ":<18}{diminuir(preco, desconto, formatacao=True):>10}''')
    print('-' * 30)
