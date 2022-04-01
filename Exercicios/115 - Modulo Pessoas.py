def cadastrarPessoa(n, i):
    try:
        arq = open('pessoas.txt', 'r')
        conteudo = arq.readlines()
        conteudo.append(f'{n}'.ljust(30) + f'{i} anos\n'.rjust(10))
        arq.close()

        arq = open('pessoas.txt', 'w')
        arq.writelines(conteudo)
        arq.close()
    except FileNotFoundError:
        arq = open('pessoas.txt', 'w')
        texto = (f'{n}'.ljust(30) + f'{i} anos\n'.rjust(10))
        arq.writelines(texto)


def imprimir():
    try:
        arq = open('pessoas.txt', 'r')
        texto = arq.read()
        print(texto)
        arq.close()
    except FileNotFoundError:
        print('*** '*10)
        
