#Faca um algoritimo que leia salario de um funcionario e mostre seu novo salario, com 15% de aumento

SA = float(input('Digite o salario actual: EUR'))
NS = SA + (SA * 15/100)
print('O novo salario com 15% de aumento fica em torno de EUR{:.2f}.'.format(NS))
