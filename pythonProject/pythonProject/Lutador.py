'''Enunciado
Escreva um programa para exibir na tela o nome e a categoria de um lutador.
O programa deve ler uma string, um número real para o peso.
Conforme o peso, ocorrerá o enquadramento  na categoria, segundo a tabela fornecida.'''
##ILUSTRANDO A FORMA COMPLETA DO COMANDO CONDICIONAL##

Nome = input('Digíte o nome do lutador: ')
Peso = float(input(f'Digite o peso do {Nome}: '))

if Peso < 52:
    Categoria = '' #String vazia significa conteúdo inválido
elif Peso < 65:
    Categoria = 'Pena'
elif Peso < 72:
    Categoria = 'Leve'
elif Peso < 79:
    Categoria = 'Ligeiro'
elif Peso < 86:
    Categoria = 'Meio-Médio'
elif Peso < 90:
    Categoria = 'Médio'
elif Peso < 100:
    Categoria = 'Meio-Pesado'
else:
    Categoria = 'Pesado'

msg = 'O lutador {} pesa {:.3f} kg e se enquadra na categoria {}'
if Categoria != '':
    print(msg.format(Nome, Peso, Categoria)) #Aqui usa-se a mensagem com string formatado sem o f string
else:
    print(f'Peso inválido: {Peso}')
print('Fim do Programa')
