# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, crie 2 listas extras que vao contar apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteudo das 3 listas geradas.
list = []
listpar = []
listimpar = []
while True:
    list.append(int(input('Digite um numero: ')))
    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta invalida, Tente Novamente...')
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp =='N':
        break

for cont in list:
    if cont % 2 == 0:
        listpar.append(cont)
    else:
        listimpar.append(cont)
print('\033[36m-=\033[m'*25)
print(f'\033[4mO Total de Numeros digitados\033[m \033[1;31m{list}\033[m')
print(f'O Total de Numeros \033[42mPARES\033[m \033[1;31m{listpar}\033[m')
print(f'O Total de Numeros \033[43mIMPARES\033[m \033[1;31m{listimpar}\033[m')