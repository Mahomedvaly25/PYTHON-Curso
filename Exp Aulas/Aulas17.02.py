# Usando o [:] para copiar os valores da variavel a para variavel b, sem criar uma ligacao entre elas
from random import randint
#a = [3,5,4,8,9]
#b = a[:]
#b[2] = 6
#print(f'A Lista A: {a}')
#print(f'A Lista B: {b}')
#print(a[len(a)])


lista = []
for n in range(0,5):
    lista.append(randint(2,40))
print(lista)
print(lista[len(lista)-1])
print(len(lista))