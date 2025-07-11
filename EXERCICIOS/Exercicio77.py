# Crie um programa que tenha uma tupla com varias palavras (nao usar acentuacao),
# Depois disso deve mostrar para cada palavra, quais sao as suas vogais.

palavras = ('Aprender','Programar','Linguagem','Python','Curso','Gratis','Estudar','praticar','trabalhar','mercado','trabalhador','futuro')
print('-'*50)
for n in palavras:
    print(f'\nNa palavra \033[33m{n.upper()}\033[m temos:{' ':<2}',end='')
    for letra in n:
        if letra in 'aeiou':
            print(f'\033[35m{letra.lower()}\033[m', end=' ')
print('\n')
print('-'*50)