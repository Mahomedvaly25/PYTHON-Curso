estado = dict()
portugal = list()

for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa:  '))
    estado['Sgl'] = str(input('Sigla do Estado:  '))
    portugal.append(estado.copy())
print('.' * 50)
for e in portugal:
    for k, v in e.items():
        print(f'{k} = {v}')
print('.' * 50)
print(portugal[0]['Sgl'])