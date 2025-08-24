''' Crie um programa que leia nomes, ano de nascimento e carteira de trabalha, cadastre-os (com idade) em um dicionario se por acaso,
a CTPS (CARTEIRA DE TRABALHO DE PROVIDENCIA SOCIAL) for diferente de Zero, o dicionario recebera tambem o ano de contratacao e o Salario.
- Calcule e acrescente para alem da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
cadastro = dict()
anoactual = date.today().year
cadastro['nome'] = str(input('Digite o nome:  '))
cadastro['Nascimento'] = int(input(f'Ano de nascimento do {cadastro["nome"]}:  '))
cadastro['Idade'] = anoactual - cadastro['Nascimento']
print(cadastro)
if cadastro['Idade'] >= 18:
    cadastro['CTrabalho'] = int(input('Indique o No. da Carteira de Trabalho: '))
    cadastro['AnoContratacao'] = int(input('Indique o ano do inicio do Contrato de trabalho?  '))
    cadastro['Salario'] = float(input('Indique o Salario:  '))
    print(cadastro['CTrabalho'])
else:
    print('Nao tem idade suficiente para trabalho')
print(cadastro)
print('Obrigado')