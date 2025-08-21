'''Enunciado
Altere o prgrama anterior para exibir o menor número inteiro, de modo
que ele continue exibindo o menor dos dois valores lidos. Agora, porém,
quando os valores forem iguais,  o programa deve exibir o valor com a
mensagem "Os dois números são iguais".
'''

a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))

if a == b:
    print(f'Os dois números são iguais e valem {b}')

elif a < b:
    print(f'O menor é número é {a}') #Outra forma de resolver o problema
#else:
    #if a < b:
     #   print(f'O menor é número é {a}') #Deve-se identar o else abaixo
else:
    print(f'O menor é número é {b}')
print('Fim do Programa')