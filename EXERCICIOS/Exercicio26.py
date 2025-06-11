#     MANIPULACAO DE STRING
# Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posicao ela aparece pela 1a vez?
# Em que posicao ela aparece pela ultima vez?

frase = str(input('Digite uma Frase qualquer: ')).strip().lower()
print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print('A posicao da 1a letra "A" aparecau na posicao {}'.format(frase.find('a')+1))
print('A letra "A" apareceu pela ultima vez na posicao {}'.format(frase.rfind('a')+1))