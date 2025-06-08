#     MANIPULACAO DE STRING
# Faca um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "Santos".

cidade = str(input('Indique a Cidade onde nasceu: ')).strip()
print(cidade[0:5].upper() == 'SANTO')