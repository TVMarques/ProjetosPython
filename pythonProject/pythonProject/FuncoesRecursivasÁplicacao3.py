#FUNÇÃO DE BUSCA BINÁRIA ##

def BuscaBin(valor, lista, ini, fim):
    '''Procura valor em lista, entre as posições ini:fim'''
    print(f'ini = {ini} e fim = {fim}')
    if ini > fim:#Valor não está na lista
        return False
    meio = (ini + fim)//2
    print(f'   meio = {meio} e o valor nessa posição é {lista[meio]}')
    if valor == lista[meio]:#Se está no meio, é o achado
        return True
    elif valor < lista[meio]:# Procura na esquerda
        return BuscaBin(valor, lista, ini, meio - 1)
    else: #Procura na direita
        return BuscaBin(valor, lista, meio + 1, fim)




l = [14, 17, 20, 22, 23, 25, 28, 29, 31, 35, 40, 45, 50, 53, 56, 59, 62, 65]
x = int(input('Digite um valor para pesquisa na lista: '))
while x != 0:
    achou = BuscaBin(x, l, 0, len(l) - 1)
    if achou != 0:
        #Chamada para verificar a metade esquerda da lista
        print(f'{x} está na lista')
    else:
        #Chamada para verificar a metade direita da lista
        print(f'{x} não está na lista')
    x = int(input('Digite um valor para pesquisa na lista: '))
print(('\nFim do Programa'))