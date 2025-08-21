def Fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * Fatorial(n - 1)

entrada = int(input('Digite um inteiro: '))
f = Fatorial(entrada)
print(f'O fatorial de {entrada} é {f}')
