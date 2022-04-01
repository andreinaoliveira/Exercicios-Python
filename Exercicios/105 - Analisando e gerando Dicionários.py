#    Exercício Python 104 - Validando entrada de dados em Python
#    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#    e vai retornar um dicionário com as seguintes informações:
#       - Quantidade de notas
#       - A maior nota
#       - A menor nota
#       - A média da turma
#       - A situação (opcional)
#    Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*nota):
    """
    Função para receber notas e retornar um dicionário contendo informações sobre a turma
    :param nota: recebe as notas da turma.
    :return: retorna um dicionário contendo a quantidade de notas informadas, a maior e menor nota, além da média da turma.
    """
    informacoes = dict()
    informacoes['Quantidade de notas'] = len(nota)
    informacoes['Maior nota'] = max(nota)
    informacoes['Menor nota'] = min(nota)
    informacoes['Média da turma'] = sum(nota)/len(nota)

    if sum(nota)/len(nota) >= 7:
        informacoes['Situação da turma'] = 'Boa'
    elif sum(nota)/len(nota) >= 5:
        informacoes['Situação da turma'] = 'Razoavel'
    else:
        informacoes['Situação da turma'] = 'Ruim'

    for i, j in informacoes.items():
        print(f'{i}: {j}')


# MAIN
notas(10, 5, 9)
