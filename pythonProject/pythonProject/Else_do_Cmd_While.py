x = 1
while x > 0:
    x = int(input('Digite X: '))
    if x == 0:
        print('  Você digitou zero ...')
        break
    print(x)
else:
    print('  Você digitou um número negativo ...')

print('Fim do Programa')