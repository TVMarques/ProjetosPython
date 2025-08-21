'''Enunciado
Escreva um programa que leia dados dos Estados bostileiros: Sigla, Nome, Capital e PIB.
A Sigla deve ser usada como chave para o dicinário e o valor deve ser um dicionário aninhado
contendo os objetos Nome, Capital, PIB. A leitura termina quando um string vazio for fornecido para a Sigla.
Exibir os dados na tela. ---Fazendo de forma diferente do anterior---'''
UF = {}
print('LEITURA DOS DADOS')
while True:
    sigla = input('Digite a sigla: ')
    if sigla == '':
        break
    elif sigla in UF:
        print(f' A sigla {sigla} já está no cadastro')
        continue
    estado = input('Digite o nome do estado do Bostil: ')
    capital = input('Digite a capital do estado bostileiro: ')
    pib = float(input('Digite o PIB:'))
    ItemDic = {'nome': estado, 'capital': capital, 'pib': pib}
    UF[sigla] =ItemDic #Dicionário aninhado, você pega os elementos de outro dicionário e coloca neste dicionário.

print('    {:20} {:15} {:>10}'.format( 'Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():#Exibição com chave e tupla em forma tabular de tupla
    print('({}) {:20} {:15} {:10.1f}'.format(
        sigla,
        dados['nome'],#Aqui dados é tratado com a chave do dicionário ItemDic
        dados['capital'],
        dados['pib'])
    )

print('\nFim do Programa ')