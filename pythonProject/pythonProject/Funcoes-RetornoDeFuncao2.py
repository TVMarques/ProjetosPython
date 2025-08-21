from random import randint
def CarregaLista():
    l = []
    for i in range(10):#Crianddo uma lista com 10 elementos apenas.
        l.append(randint(1, 1000))#Gera valores aleatórios que vão de um a mil e os coloca na lista.
    return l

print('Início do Programa')
print('Primeira lista gerada')
valores = CarregaLista()#Atribuindo o valor de retorno da função ao objeto valores
print(f'Lista gerada >> {valores}')

#Gerando uma nova lista gerada aleatóriamente
print('Segunda lista gerada')
valores2 = CarregaLista()#Atribuindo o valor de retorno da função ao objeto valores
print(f'Lista gerada >> {valores2}')
print('Fim do Programa')