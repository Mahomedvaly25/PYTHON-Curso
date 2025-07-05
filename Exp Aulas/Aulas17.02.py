# Usando o [:] para copiar os valores da variavel a para variavel b, sem criar uma ligacao entre elas

a = [3,5,4,8,9]
b = a[:]
b[2] = 6
print(f'A Lista A: {a}')
print(f'A Lista B: {b}')