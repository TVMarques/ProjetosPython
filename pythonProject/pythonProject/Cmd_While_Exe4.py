'''Enunciado
Escreva um programa que leia do teclado um número inteiro D. Esse número deve
ser obrigatoriamente maior que zero. Em seguida exiba na tela todos os números
inteiros menores que 100 e que sejam divisíveis por D.'''

d = int(input('Digite D: '))
if d <= 0:
    print(f'O valor {d} é inválido !!')
else:
    i = 1
    while i < 100:
        if i % d == 0: #Se i que, começa por 1, for divisível por d, então o i é exibido na tela.
            print(i, end='  ')#Exibe os elementos na mesma linha, com 2 espaços em branco.
        i += 1

print('\n\nFim do Programa')