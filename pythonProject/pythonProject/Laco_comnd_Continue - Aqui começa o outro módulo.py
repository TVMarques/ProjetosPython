'''Comando continue no laço WHILE: Este comando tem como objetivo interromper
um comando de repetição na instância'''
i = 0
while i < 40:
    i = i +1
    if i % 4 == 0: #Printando todos os números NÃO dvisíveis por 4, colocando x nos divisíveis. ##i == 4:Outra forma de fazer
        print('x', end=' ')#Exibindo o x no lugar do divisível por 4
        continue #O camando continue interrompe a execução do laço, quando ele chega na iteração 4 e continua ao seguinte
    print(i, end='  ')#O 'end' suprime o pulo de linha
