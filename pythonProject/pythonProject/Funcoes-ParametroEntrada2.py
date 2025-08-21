from random import randint
#Generalizando (tornando genérico) o uso da função.
def CarregaLista(qtde, a, b):#Chamador da função
    ''' Carrega uma lista com qtde elementos inteiros aleatórios entre a e b escolhidos pelo o usuário.'''
    l = []
    for i in range(qtde):
        l.append(randint(a, b))
    return l

q = int(input('Digite a quantidade desejada de elementos: '))
lmin = int(input('Digite o limite mínimo: '))
lmax = int(input('Digite o limite máximo: '))
valores = CarregaLista(q, lmin, lmax)
print(f'Lista gerada >> {valores}')

print(f'A lista gerada tem {q} elementos')

print('Fim do Programa')