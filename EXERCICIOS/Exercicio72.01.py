# CORRECAO DE PROFESSOR

extenso = ('Zero','Um','Dois','Tres','Quarto','Cinco',
           'Seis','Sete','Oito','Nove','Dez','Onze','Doze',
           'Treze','Quatorze','Quinze','Dezesseis',
           'Dezessete','Dezenove','Vinte')
while True:
    numero = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente', end=' ')
print(f'Voce digitou o numero {extenso[numero]}')
