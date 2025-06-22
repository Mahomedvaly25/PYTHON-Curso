n = int(input('Digite um numero: '))
f = 1
c = n
print('CALCULANDO... {}! = '.format(n), end=' ')
for c in range(n,0,-1):
    print(c , end=' ')
    print('x' if c > 1 else '=', end=' ')
    f = f * c
    c = c - 1
print(f)