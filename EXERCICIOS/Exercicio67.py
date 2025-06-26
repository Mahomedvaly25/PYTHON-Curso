# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa sera interropido quando o numero digitado for negativo.
valor = resultado = cont = 0
while True:
    valor = int(input('Quer ver a Tabuada de qual valor: '))
    if valor < 0:
        break
    else:
        for cont in range(0,10):
            cont += 1
            resultado = valor * cont
            print(f'{valor} x {cont} = {resultado}')
print('FIM')
