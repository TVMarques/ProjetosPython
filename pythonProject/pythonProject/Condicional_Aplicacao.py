''' Enunciado
Escreva um programa que leia um número inteiro e mostre na tela
se ele é par ou ímpar.
Lembrando que para saber a paridade de um inteiro, é preciso calcular
o resto da sua divisão por 2. Se o resto for 0, o número é par,
se for 1, é ímpar.  '''

x = int(input('Digite um número inteiro: '))

#resto = x % 2
#if resto == 0:

if x % 2 == 0: #Outra forma de fazer o if com o mesmo resultado, juntando as condições acima
    print(f'{x} é um número par !!')

else:
    print(f'{x} é um número ímpar !!')

print('Fim do Programa')