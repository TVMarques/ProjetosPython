'''Enunciado
Escreva um programa que utilize uma função recursiva para realizar uma contagem regressiva.
Este programa deve ler do teclado um inteiro que represente a quantidade de toques dessa contagem
regressiva. Quando a conntagem chegar em zero, o programa deve exibir na tela a mensagem "NO AR !!"'''
from time import sleep #Biblioteca importada para se ter parada de tempo
def Contagem(cont):
    if cont == 0:
        print('Mesmo que seu televisor ainda não seja PHILLIPS, você verá a Copa com a PHILLIPS !!!')
    else:
        print(cont)
        sleep(1)
        Contagem(cont - 1)


toques = int(input('Digite a quantidade de toques: ')) # toques = 8
print(f'Atenção emissoras componentes da Rede Globo para o top de {toques} segundos !! As imagens da Copa serão geradas para o mundo por câmeras PHILLIPS.')
sleep(8)
Contagem(toques)