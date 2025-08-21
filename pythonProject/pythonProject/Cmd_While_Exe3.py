'''Enunciado
Escreva um programa que mostre na tela os 10 primeiros termos de uma
progressão aritimética (PA) com primeiro termo P e razão R.
Os dois números P e R são inteiros e devem ser lidos do teclado. '''

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

#Exemplo do que é progressão aritimética
#Suponha que P = 4 e R = 3;
#O resultado do print dos 10 primeiros termos da PA seriam:
#4, 7, 10, 13, 16, 19, 22, 25, 28, 31.

cont = 1
while cont <= 10:
    print(p, end=', ')
    p = p + r
    cont += 1 #é o mesmo que cont = cont + 1

print('\nFim do Programa')