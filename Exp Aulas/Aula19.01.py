veiculos = list()
carros = dict()
for c in range(0,3):
    carros['Marca'] = str(input('Marca do carro: '))
    carros['Modelo'] = str(input('Qual o Modelo: '))
    veiculos.append(carros.copy())
print('.' * 50)
for car in veiculos:
    for v in car.values():
        print(f'{v}',end=' ')
    print()
print('.' * 50)
for car in veiculos:
    for k, v in car.items():
        print(f'{k} = {v};', end=' ')
    print()