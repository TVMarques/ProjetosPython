'''Enunciado
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0.
Todos os valores digitados, exceto o  zero, devem ser gravados em um arquivo em disco,
um por linha, com três casas decimais.
Usar método .wriitelines().'''
Lst = []
x = float(input('Digite um número real: '))
while x != 0:
    Lst.append(f'{x:.3f}\n')#Coloca na lista com o append o número com três casas decimais e pulando uma linha. Lembrando que o número é trasnformado em string pelo fstring devido o write.
    x = float(input('Digite um número real: '))

print(Lst)
arq = open('saida_exercicio2.txt', 'w')
arq.writelines(Lst)#Este método tem a propriedade de gravar múltiplas linhas em uma única operação. O argumento passado aqui precisa ser string.
arq.close()
print('\nFim do Programa')