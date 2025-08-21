#CODFICAÇÃO DOS ARRQUIVOS TEXTOS

codGravacao = input('Digite a codificação de Gravação: ')
codLeitura = input('Digite a codificação de Leitura: ')

print('Etapa de gravação do arquivo')
arq = open('codificacao.txt' , 'w', encoding=codGravacao) #O arquivo será gravaddo com o código ANSI ou UTF-8 digiitados na primeira linha.
arq.write('Gravação do Arquivo\n')#Aquilo o que será gravado no meu arquivo.
arq.write('acentos: á, é í, Á, É, Í, ç, Ç\n')#Aquilo o que será gravado no meu arquivo.
arq.close()

print('\nEtapa de leitura do arquivo')
arq = open('codificacao.txt', 'r', encoding=codLeitura)#Lendo o arquivo gravado com um código de leitura digitado.
s = arq.readline()
print(s.rstrip())
s = arq.readline()
print(s.rstrip())
arq.close()

print('Fim do Programa')
