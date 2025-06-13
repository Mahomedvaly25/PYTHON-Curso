# CONDICOES EM PYTHON
# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superior a 1250,00 Euros, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento e de 15%

salario = float(input('Digite o Salario actual: '))
if salario <= 1250:
    Nsalario = salario + (salario * 15/100)
else:
    Nsalario = salario + (salario * 10/100)
print('Com Base no salario de {}, o novo salario passa a ser {}'.format(salario,Nsalario))