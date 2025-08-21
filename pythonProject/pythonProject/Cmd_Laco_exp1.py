'''Enunciado
Escreva um programa que em laço enquanto um valor x lido for diferente
de zero. Para cada valor de x, apresente na tela se é par ou impar.'''
#ELEMENTOS DO CONTROLE DE LAÇO
#1° Situação inicial de controle
#2° Condição de continuidade
#3° Alteração no objeto de controle a cada repetição

x = 1
while x != 0:
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        print(f'{x} é par.')
    else:
        print(f'{x} é impar.')
print('Fim do Programa')