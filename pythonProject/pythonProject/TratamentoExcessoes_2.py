try:
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    r = a / b
    print(r)
except ZeroDivisionError:
    print('O valor de B não pode ser zero.')
except ValueError:
    print('Digite números inteiros para A e B')
except: #except genérico.
    print('Não é possível calcular a divisão !!')
print('Fim do Programa')