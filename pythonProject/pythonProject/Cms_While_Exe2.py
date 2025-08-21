'''Enunciado
Escreva um programa que mostre na tela a tabuada do número inteiro N
que deve ser lido do teclado.'''
n = int(input('Digite N: '))
cont = 1
while cont <= 10:
    #r = cont * n
    print(f'{n} x {cont} = {cont * n}') #Neste {cont * n}, pode colocar r e descomentar o código acima
    cont = cont + 1

print('Fim do Programa')
