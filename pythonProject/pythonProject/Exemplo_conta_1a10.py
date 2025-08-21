'''Quantos destes fragmentos apresentam uma contagem progressiva, iniciada em 1 e finalizada em 10?'''

cont = 0
while cont < 10:
    cont += 1
    print(cont)
print('-------------')

cont = 1
while cont < 10:
   print(cont)
   cont = cont + 1

print('-------------')
cont = 10
while cont > 0:
    cont = cont - 1
    print(10 - cont)

print('-------------')

cont = 0
while cont < 10:
    print(cont + 1)
    cont = cont + 1
