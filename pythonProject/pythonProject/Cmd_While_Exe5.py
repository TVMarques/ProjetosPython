'''Enunciado
Escreva um programa que permaneça em laço enquanto um valor inteiro lido for
diferente de zero. Totalize e conte os valores digitados, exceto o zero, e
apresente na tela esses valores. Totalizar é somar os valores.  '''
#Caso de teste
#16 40 21 6: Total 83 - Quantidade : 83
soma = qtde = 0
#Deixando o while desta forma, temos a aquisição do dado na saída do laço.
a = int(input('Digite um valor: '))
while a != 0:
    soma = soma + a
    qtde = qtde + 1
    a = int(input('Digite um valor: '))


print(f'Soma dos valores é igual = {soma}')
print(f'Quantidade = {qtde}')
print('Fim do programa')


'''cont = 0
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
    cont = cont + 1'''
