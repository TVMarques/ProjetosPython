'''Enunciado
Escreva um programa que leia três números inteiros: o primeiro termo P, a razão R e a
quantidade Q de termos de uma progressão aritimética. O programa deve calcular os Q
termos da progrssão colocando-os em uma lista e no final exibi-la na tela.
obs: esse problema já foi abordado, sem o uso de listas, no exercício Cmd_While_Exe3'''
#Exemplo do que é progressão aritimética
#Suponha que P = 4 e R = 3;
#O resultado do print dos 10 primeiros termos da PA, se o Q for igual a 10 por exemplo, seriam:
#4, 7, 10, 13, 16, 19, 22, 25, 28, 31.


P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
Q = int(input('Digite a quantidade de termos: '))
#Usando lista
#Termos = [P]#Se para adicionar um valor na lista for colocado abaixo do contador, é preciso iniciar a lista com um termo, no caso o P
Termos = []
cont = 0
while cont < Q: #-1 se for da outra forma
    Termos.append(P)  # É preciso que a lista tenha o primeiro valor. obs: Pode-se colocar esta linha abaixo do contador de P.
    P = P + R
    cont += 1 #é o mesmo que cont = cont + 1
print('\nLista Resultante')
print(Termos)
print('\nFim do Programa')