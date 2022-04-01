#   Exercício Python 056 - Analisador completo
#   Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#   No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
#   e quantas mulheres têm menos de 20 anos.

soma_idade = 0
homem_idade = 0
homem_nome = ''
c_mulheres = 0

for i in range(1, 5):
    print("----- {}º Pessoa -----".format(i))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))

    soma_idade += idade

    if sexo in 'Mm' and idade > homem_idade:
        homem_idade = idade
        homem_nome = nome

    if sexo in 'Ff' and idade < 20:
        c_mulheres += 1

print("A média de idade do grupo é de {:.1f}".format(soma_idade / 4))
print("O homem mais velho tem {} anos e se chama {}".format(homem_idade, homem_nome))
print("Ao todo são {} mulheres com menos de 20 anos".format(c_mulheres))
