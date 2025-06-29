# RESOLVIDO COM A OPCAO DE QUER CONTINUAR OU NAO

extenso = ('Zero','Um','Dois','Tres','Quarto','Cinco',
           'Seis','Sete','Oito','Nove','Dez','Onze','Doze',
           'Treze','Quatorze','Quinze','Dezesseis',
           'Dezessete','Dezenove','Vinte')
while True:
    resp = ' '
    numero = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= numero <= 20:
        print(f'Voce digitou o numero {extenso[numero]}')
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    else:
        print('Numero invalido, Tente novamente', end=' ')
    if resp == 'N':
        break
print('OBRIGADO, VOLTE SEMPRE!!!')