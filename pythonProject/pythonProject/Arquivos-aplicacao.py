'''Enunciado
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0.
Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
Usar o método  .write()'''
arq = open('saida_exercicio.txt', 'w')#Abrindo o arquivo para escrever nele com o método write.
a = int(input('Digite um inteiro: '))
while a != 0:
    arq.write(f'{a}\n')#O write NÃO escreve objetos inteiros, só string, por isso se colocou o objeto a dentro do fstring. O \n é obrigatório no write, assim ficará com pulo de linha no arquivo.
    a = int(input('Digite um inteiro: '))
arq.close()#aqui se garante que o arquivo será fechado e finalizado


print('\nFim do Programa')