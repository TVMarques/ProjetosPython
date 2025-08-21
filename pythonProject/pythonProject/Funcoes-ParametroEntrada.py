from random import randint
#Generalizando (tornando genérico) o uso da função.
def CarregaLista(qtde):#Chamador da função
    ''' Carrega uma lista com qtde elementos inteiros aleatórios entre 1 e 1000.'''
    l = []
    for i in range(qtde):#Crianddo uma lista com a qtde de elementos vindos do chamador da função.
        l.append(randint(1, 1000))#Gera valores aleatórios que vão de um a mil e os coloca na lista.
    return l

q = int(input('Digite a quantidade desejada de elementos: '))
valores = CarregaLista(q)#Assim a lista será carregada com a quantidade desejada de elementos.
print(f'Lista gerada >> {valores}')

print(f'A lista gerada tem {q} elementos')

print('Fim do Programa')
