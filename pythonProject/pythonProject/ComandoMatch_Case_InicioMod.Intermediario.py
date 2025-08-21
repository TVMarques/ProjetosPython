#Match case --> Comando condicional múltiplo
n = -1
while n != 0:
    n = int(input('Digite um inteiro: '))
    match n:
        case 0:
            print(' Você digitou o :')
        case 1:
            print(' você digitou um')
        case 2:
            print(' você digitou dois')
        case 3:
            print(' você digitou três')
        case _:#Obrigatóriamente, esta clausula case precisa ser a ultima diferente das anteriores que podem variar
            print(' você digitou outro número')

print('\n\nFim do programa')
