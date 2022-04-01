#    Exercício Python 106 - Sistema interativo de ajuda em Python
#    Faça um mini-sistema que utilize o Interactive Help do Python.
#    O usuário vai digitar o comando e o manual vai aparecer.
#    Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.


def ajuda(funcao):
    print('\033[7m~' * 30)
    help(funcao)
    print('\033[m' * 30)


while True:
    print('\033[45m~'*30)
    print(f'{"Sistema de ajuda PyHELP":^30}')
    print('~' * 30)
    print('\033[m')

    aux = (str(input('Função ou Biblioteca (FIM para sair)-> ')))
    if aux == 'FIM':

        break

    ajuda(aux)
