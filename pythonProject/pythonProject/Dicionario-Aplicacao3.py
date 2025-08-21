'''Enunciado
Escreva um programa que leia dados dos Estados bostileiros: Sigla, Nome, Capital e PIB.
A Sigla deve ser usada como chave para o dicinário e o valor deve ser uma tupla formada
com (Nome, Capital, PIB). A leitura termina quando um string vazio for fornecido para a Sigla.
Exibir os dados na tela.'''
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
    UF[sigla] = (estado, capital, pib)

print('\nDados dos Estados')#Exibição de forma simplória
for item in UF.items():
    print(item)

print('----------------------------------------------------------------------------\n')

print('    {:20} {:15} {:>10}'.format( 'Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():#Exibição com chave e tupla em forma tabular de tupla
    print('({}) {:20} {:15} {:10.1f}'.format(
        sigla,
        dados[0],
        dados[1],
        dados[2])
    )

print('\nFim do Programa ')