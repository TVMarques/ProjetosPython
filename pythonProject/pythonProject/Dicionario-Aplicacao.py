'''Enunciado
Escreva um programa que leia do teclado o código de um produto e seu preço unitário.
O código é um string e o preço é real. Acrescente o par código: preço em um dicionário.
O laço termina quando for fornecido um string vazio para o código. Ao final, exibir código
e preço, um produto em cada linha. '''

produtos = {}
print('Leitura dos dados')
cod = input( 'Digite o código: ')
while cod != '':
    preco = float(input(' Digite o preço: '))
    produtos[cod] = preco
    cod = input('Digite o código: ')

print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys():#Pode-se usar o .values no luggar de .keys
    print(f' produto {cod} custa R$ {produtos[cod]:.2f}')#Este :7.2f faz ter casa decimal

print('FIM DO PROGRAMA')