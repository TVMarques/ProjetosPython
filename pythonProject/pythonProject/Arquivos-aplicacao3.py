'''Enunciado
Escreva um programa que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela.
Mostrar também a soma dos valores, a quantidade, a média aritimética, o menor valor e o maior valor.
Usar um laço while e na leitura o método .readline().'''

Lst = []
arqEnt = open('entrada1.txt','r') #Abrindo o arquivo e lendo o conteúdo dele com o r de read
linha = arqEnt.readline()#Este comando lê todo o conjunto de linhas do arquvo.
while linha != '': #Enquando a linha for diferente de vazia, acrescente na lista uma linha lida do arquivo.
    Lst.append(int(linha))
    linha = arqEnt.readline()#Lê o próximo valor do arquivo.
arqEnt.close()

print('Lista lida do arquivo --->')
print(Lst)
soma = sum(Lst) #Esta função calcula a soma dos elementos da lista
print(f'Soma dos valores = {soma}')
qtde = len(Lst)  #Esta função determina a quantidade dos elementos da lista
print(f'Quantidade = {qtde}')
print(f'Média dos valores = {soma/qtde}') #Cáculo para se ter a média dos valores da lista.
minimo = min(Lst)  #Esta função determina o menor elemento da lista.
print(f'Menor dos valores = {minimo}')
maximo = max(Lst)  #Esta função determina o maior elemento da lista.
print(f'Maior dos valores = {maximo}')

print('\nFim do Programa')