def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO: Digite um numero inteiro valido.\033[me')
        if ok:
            break
    return n

n = leiaInt('Digite um numero: ')
print(f'O Numero degitado foi {n}')