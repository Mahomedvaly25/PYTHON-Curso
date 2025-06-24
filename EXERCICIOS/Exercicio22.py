#     MANIPULACAO DE STRING
# Crie um programa que leie o nome completo de uma pessoa e mostre:
#  - O nome com todas as letras maiusculas.
#  - O nome com todas as letras menusculas.
#  - Quantas letras ao td sem considerar espacos.
#  - Quantas letras tem o 1o Nome?

nome =  input('Digite o nome completo: ').strip()
print('+'*50)
print('ANALISE DO NOME: **',nome,'**')
print('Tornando as letra em Maiusculas: ',nome.upper())
print('Tornando as letra em Menusculas: ',nome.lower())
print('O Nome ',nome,' tem {} letras ao todo'.format(len(nome) - nome.count(' ')))
print('O seu 1o nome tem {} letras'.format(nome.find(' ')))
# OU
separa = nome.split()
print('O seu primeiro Nome e {} e ele tem {} letras '.format(separa[0], len(separa[0])))