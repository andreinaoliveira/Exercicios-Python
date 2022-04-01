#   Exercício Python 077 - Contando vogais em Tupla
#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')

for palavra in frutas:
    print(f'Palavra {palavra.upper()} \nVogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n')
