#     MANIPULACAO DE STRING
# Faca um programa que leia o nome completo de uma pessoa, e mostrando em seguida o primeiro e o ultimo nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Ola ', nome,'!')
nome = nome.split()
print('O seu nome completo tem {} partes'.format(len(nome)))
print('O Seu primeiro nome: {}'.format(nome[0]))
print('O Seu ultimo nome: {}'.format(nome[len(nome)-1]))