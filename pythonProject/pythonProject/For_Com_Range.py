'''Enunciado
Escreva um programa que leia um número inteiro N. Em seguida leia N números reais
carregando-os em uma lista. Ao final exiba os elementos da lista na tela,
sendo um em cada linha. '''
n =  int(input('Digite a quantidade: '))#Digite  a quantidade de elementos para ser digitados
l = []
for i in range(n):
    x = float(input(f' elemento {i}: '))#Para cada elemento i coloque na lista l os valores float x
    l.append(x)#Comando para colocar os valores na lista l

print('\nResultado')

for valor in l:#Para cada valor da lista l, exiba:
    print(f' {valor:.2f}')#.2f faz exibir os elementos com duas casas decimais

print('Fim do programa')