'''Enunciado
Escreva um programa que leia um arquivo de entrada carregando seus dados em um dicionário e
ao final exibindo-os na tela. A figura 11.1 mostra do lado esquerdo a natureza dos dados que
serão lidos e do lado direito mostra o formato do arquivo.
Esse formato é conhecido comm CSV. Arquivos CSV são muito usados em diversas áreas da computação,
em especial na Análise de Dados. O que caracteriza um arquivo CSV é que cada linha tem um
conjunto de dados de alguma forma relacionados e separados por um caractere delimitador.
No arquivo deste exercício o delimitador é um ponto-e-vírgula ";"
Neste caso, cada linha tem: código de produto (int), a quantidade em estoque (int), preço (float). Use o '''

estoque = {}
for linha in open('entrada2.txt','r'):
    #s = linha.rstrip()#Suprimindo o caractere de pulo de linha vindo da leitura do arquivo.
    #lst = s.split(';')#Separando o conteúdo de s pelo ;. Assim o dado vira uma lista.
    lst = linha.rstrip().split(';')#Está forma mais compacta se utiliza dos dois comandos acima juntos. É uma forma mais usada.
    print(lst)#, end='...')#Lendo cada linha do arquivo e não tendo o pulo da linha mas tendo  3 pontos ... para cada linha.
    cod = int(lst[0])#Convertendo o primeiro índice da lista do arquvo entrada2 para int.
    qtde = int(lst[1])#Convertendo o segundo índice para inteiro.
    pcunit = float(lst[2])#Convertendo o terceiro índice para float.
    estoque[cod] = (qtde, pcunit)#Colocando no dicionário o par chave e valor vindos do arquivo, com os valores na forma de tuplas.

print('Valores carregados no Dicionário')
print(estoque)

print('\nExibição dos dados na forma de tabela')
totGeral = 0
for cod, dados in estoque.items():#O .items() vai retornar do dicionário o cod e a tupla de dados.
    tot = dados[0] * dados[1]#Calculando a multiplicação do indice 0 a qtde e indice 2, o pcunit do dicionário.
    totGeral += tot#Agregando o valor de tot em totGeral. Na prática seria: totGeral += dados[0] * dados[1]
    print(f' {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot: 8.2f}')
print(' ' * 24, f'{totGeral:8.2f}')
print('\nFim do Progrma')