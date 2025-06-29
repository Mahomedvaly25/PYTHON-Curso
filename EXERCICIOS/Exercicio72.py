# Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de 0 ate 20
# Seu programa devera ler um numero pelo teclado entre 0 a 20 e mostra-lo por extenso.

extenso = ('Zero','Um','Dois','Tres','Quarto','Cinco',
           'Seis','Sete','Oito','Nove','Dez','Onze','Doze',
           'Treze','Quatorze','Quinze','Dezesseis',
           'Dezessete','Dezenove','Vinte')
numero = int(input('Digite um Numero entre 0 a 20: '))
while numero > 20 or numero < 0:
    numero = int(input('Tente Novamente, digite um Numero entre 0 a 20: '))
print(f'Voce digitou o numero {extenso[numero]}')
