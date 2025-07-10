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

print(list)
print(listpar)
print(listimpar)