'''Enunciado
Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e
retorne True se A for divisível por B e False caso contrário.
Escreva o programa principal para testar a função.'''

def Divisivel( A, B):
    return True if A % B == 0 else False

valorA = int(input('Digite A: '))
valorB = int(input('Digite B: '))

if Divisivel(valorA, valorB):#Colocando a função como condição no comando if.
    print(f'{valorA} é divisível por {valorB}')
else:
    print(f'{valorA} não é divisível por {valorB}')
