# Crie um programa que vai ler varios numeros e colocar em uma lista, depois disso mostre:
# a) Quantos numeros foram digitados.
# b) A lista de valores, ordenada em ordem decrescente
# c) Se o valor 5 foi digitado e esta ou nao na lista.

quant = 0
list = []
while True:
    list.append(int(input('Digite um numero: ')))

    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta invalida, Tente Novamente.')
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

list.sort(reverse=True)
print('-='*30)
print(f'Voce digitou \033[1;33m{len(list)}\033[m elementos.')
print('-='*30)
print(f'Os Valores em ordem Decrescente sao: \033[1;33m{list}\033[m')
print('-='*30)
if 5 in list:
    print('O Valor \033[1;33m(5)\033[m faz parte da lista.')
else:
    print('O Valor \033[1;31;m(5)\033[m nao foi encontrado na lista.')
print('-='*30)