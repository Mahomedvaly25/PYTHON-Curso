# Densevolva um logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 ate 30: Sobrepeso
# - 30 ate 40: Obesidade
# - Acima de 40: Obesidade Morbita

peso = float(input('Informe o seu PESO:' ))
altura = float(input('Informe a sua Altura: '))
imc =  peso / ( altura ** 2 )

print('O IMC conforme os dados colhidos é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do Peso Normal.')
elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa do Peso NORMAL.')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE.')
elif imc >= 40:
    print('Voce esta em OBESIDADE, CUIDADO!!!')
