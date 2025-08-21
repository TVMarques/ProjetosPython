'''Enunciado
Escreva um programa que leia um número inteiro N. Em seguida leia N números inteiros
carregando os valores negativos em uma lista e os positivos em outra. Ao final exiba na
tela cada uma das listas juntamente como seu tamanho.
 obs: Se o valor zero for fornecido ele deve ser incluído na lista de positivos.'''
n = int(input('Digite a quantidade: '))#Digitando a quantidade de elemntos a escrever
lNeg = []
lPos = []

for i in range(n):#Para cada i da qantidade de elemento digitados em n, faça:
    x = int(input(f' elemento {i} >> '))
    if x >= 0:
        lPos.append(x)#se x for maior que zero, coloca na lista positivo
    else:
        lNeg.append(x)#Coloca na lista negativa
        
print(f'\nLista de negativos: {lNeg}, contém {len(lNeg)} elementos')
print(f'\nLista de positivos: {lPos}, contém {len(lPos)} elementos')
print('Fim do programa')