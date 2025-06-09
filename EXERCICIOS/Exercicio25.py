#     MANIPULACAO DE STRING
# Crie um programa que leia nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite o nome completo: '))
print('Seu nome tem Silva? : ','silva' in nome.lower())