'''Enunciado
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X
for maior que zero. Para cada valor X verifique se ele está ou não na lista gerada.
Caso esteja, é preciso exibir a quantidade de ocorrências.'''
from random import  randint
#Primeira parte - Geração da lista
List = []
Qtde = int(input('Digite a quantidade: '))
for i in range (Qtde):
    List.append(randint(1, 20))
print('Lista Gerada')
print(List)
#Segunda parte - pesquisa na lista
X = 1
while X > 0:
    X = int(input('Digite X: '))
    if X in List:
        print(f' Há {List.count(X)} ocorrência(s) de {X} na lista')
    else:
        print(f' {X} não está na lista')
print('Fim do Programa')