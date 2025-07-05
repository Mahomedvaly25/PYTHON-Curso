valores = list()
resp = 'S'
while resp == 'S':
    valores.append(int(input('Digite Valores: ')))
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    print('_'*20)
print(valores)

