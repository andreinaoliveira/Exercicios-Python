#    Exercício Python 111 - Transformando módulos em pacotes
#    Dentro do pacote que criamos no desafio 111, temos um módulo chamado dado.
#    Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
#    mas com uma validação de dados para aceitar apenas valores que seja monetários.

from pacote.moeda import resumo
from pacote import dados

preco = dados.leiaDinheiro()
aumento = int(input('Informe a porcentagem de aumento: '))
desconto = int(input('Informe a porcentagem de desconto: '))
resumo(preco, aumento, desconto)
