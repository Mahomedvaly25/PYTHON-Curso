''' Crie um programa que leia nomes, ano de nascimento e carteira de trabalha, cadastre-os (com idade) em um dicionario se por acaso,
a CTPS (CARTEIRA DE TRABALHO DE PROVIDENCIA SOCIAL) for diferente de Zero, o dicionario recebera tambem o ano de contratacao e o Salario.
- Calcule e acrescente para alem da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
cadastro = dict()
anoactual = date.today().year
cadastro['nome'] = str(input('Digite o nome:  '))
AnoNascimento = int(input(f'Ano de nascimento do {cadastro["nome"]}:  '))
cadastro['Idade'] = anoactual - AnoNascimento
cadastro['CTrabalho'] = int(input('Numero de Carteira de Trabalho [Clique 0 se nao tiver]:  '))
if cadastro['CTrabalho'] != 0:
    cadastro['AnoContratacao'] = int(input('Indique o ano do inicio do Contrato de trabalho?  '))
    cadastro['Salario'] = float(input('Indique o Salario: $'))
    cadastro['aposentadoria'] = (cadastro['AnoContratacao'] + 35) - AnoNascimento
else:
    print('Nao tem idade suficiente para trabalho')
print('-=' * 30)
for k,v in cadastro.items():
    print(f'   - {k} = {v}')
print()
print('Obrigado')