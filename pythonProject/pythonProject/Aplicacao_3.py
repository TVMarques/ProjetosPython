'''Enunciado
Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando
for digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista,
desde que ele ainda não esteja lá, ou seja, valores repetidos não são aaceitos.
Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela.
Ao finnal exiba a lista e a quantidade de elementos que ela comtém.'''
listValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in listValores:
        listValores.append(valor)
    else:
        print(f' ERRO !! O valor {valor} já está na lista')
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(listValores)
print(f'A lista comtém {len(listValores)} elementos')
print('Fim do Programa')