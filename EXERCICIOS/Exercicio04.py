#Qc = Quantidade
Qc = input('Digite qualquer coisa: ')
print('Tipo primitivo de valor: ',type(Qc))
print('So tem espacos: ',Qc.isspace())
print('E um numero?: ',Qc.isnumeric())
print('E Alfabetico?: ',Qc.isalpha())
print('E Alfanumerico?: ', Qc.isalnum())
print('Esta em MAIUSCULAS?: ',Qc.isupper())
print('Esta em menusculas?: ',Qc.islower())
print('Esta Capitalizada?: ',Qc.istitle())
print('E um digito?: ',Qc.isdigit())
