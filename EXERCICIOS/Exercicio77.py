# Crie um programa que tenha uma tupla com varias palavras (nao usar acentuacao),
# Depois disso deve mostrar para cada palavra, quais sao as suas vogais.

palavras = ('Aprender','Programar','Linguagem','Python','Curso','Gratis','Estudar','praticar','trabalhar','mercado','trabalhador','futuro')
print('-'*50)
for n in palavras:
    print(f'\nNa palavra {n.upper()} temos:{' ':<2}',end='')
    for letra in n:
        if letra in 'aeiou':
            print(f'{letra.lower()}', end=' ')
print('\n')
print('-'*50)