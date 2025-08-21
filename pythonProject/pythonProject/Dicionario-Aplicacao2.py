'''Enunciado
Escreva um programa que leia do teclado o código de um par e seu preço unitário.
O código é um string e o preço é real. Acrescente o par código:preço em um dicionário.
O programa deve verificar se o código ja está no dicionário e neste caso deve emitir
uma mensagem de erro. O laço termina quando for fornecido um string vazio para o código.
Ao final, exibir código e preço, um produto em cada linha.'''

produtos = {}
print('Leitura dos dados')

while True:
    cod = input('Digite o código: ')
    if cod == '':
        break
    elif cod in produtos:
        print(f'  ...o código {cod} já existe !') #Exibindo uma mensagem de erro para mostrar que o  código já existe no dicionário.
        continue
    preco = float(input(' Digite o preço: '))
    produtos[cod] = preco #Aqui acrescenta o preço no dicionário produtos.


print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys():#Pode-se usar o .values no luggar de .keys
    print(f' produto {cod} custa R$ {produtos[cod]:.2f}')#Este :7.2f faz ter casa decimal

print('FIM DO PROGRAMA')