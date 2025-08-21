'''Enunciado
Escreva um programa que leia dois inteiros e mostre na tela apenas o menor
dos dois. Se ambos forem iguais, mostre qualquer um deles. '''
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))

if a <= b:
    print(f'O menor é número é {a}')

else:
    print(f'O menor é número é {b}')
print('Fim do Programa')

