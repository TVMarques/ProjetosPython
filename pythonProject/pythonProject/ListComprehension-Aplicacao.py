'''Enunciado
Considere que você deve aplicar um aumento percentual a todos os preços que estão em uma lista.
Escreva um programa que leia essa lista do teclado. Os valores devem ser lidos enquanto não for
digitado zero. Na sequência leia a porcentagem de aumento.
Em seguida, usando list comprehension, faça a aplicação desse aumento a todos os valores e mostre na tela.'''

Precos = []
print('Forneça os preços para a lista. Zero para terminar.')
preco = float(input(' digite um valor real:'))
while preco != 0:
    Precos.append(preco)
    preco = float(input(' digite um valor real:'))

print('Os preços são estes: ')
print(Precos)

aumento = float(input('Digite a porcentagem de aumento %: '))
NovosPrecos = [valor * (1 + aumento/100) for  valor in Precos if valor < 100] #Cada valor de Precos terá seu valor incrementado pelo aumento percentual. Colocando um filtro no final.
for valor in NovosPrecos:
    print(f'{valor:.2f}')

print('Fim do Prgrama')