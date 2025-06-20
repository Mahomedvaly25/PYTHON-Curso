# Faca um programa que leia o sexo de uma pessoa, mais so aceite os valores 'M' ou 'F'.
# Caso esteja errado, faca a digitacao normalmente ate ter um valor correto.

sexo = str(input('Digite o SEXO: [M/F]'))
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos.Digite Novamento o Sexo: [M/F]  ')).upper().strip()[0]
print('Sexo {} Registado com Sucesso.'.format(sexo))