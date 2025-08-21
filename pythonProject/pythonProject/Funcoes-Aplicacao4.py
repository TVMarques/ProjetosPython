'''Enunciaddo
Escreva uma função e como parâmetro de entrada dois números reais Max e Min. Essa função
deve ler do teclado um número real e retorná-lo caso esteja dentro do intervalo fechado [Min, Max].
Caso contrário, a função deve exibir uma mensagem de erro e ler um novo valor.'''

def LeReal(pLmin, pLMax):
    a = float(input('Digite um valor real: '))
    while a < pLmin or a > pLMax:#Se o valor a for menor que o valor mínimo ou maior que o valor máximo, então se lê de novo.
        print(f'O valor {a} está fora dos limítes [{pLmin}, {pLMax}]')
        a = float(input('Digite um valor real: '))#Se a linha acima for verdadeira, se lê novamente o valor de a.
    return a

#Código principal
LMin = float(input('Digite o valor mínimo: ')) #Diferença de parâmetros aqui no escopo global.
LMax = float(input('Digite o valor máximo: '))

controle = 's'
while controle == 's' or controle =='S':
    valor = LeReal(LMin, LMax)#Colacando outra vez, os valores são atribuidos nas variáveis LMin e Lmax, que por sua vez, são associadas aos argumentos da função LeReal
    print(f'O valor lido é {valor}')
    controle = input('\nQuer digitar outro valor (s/n)?')#Perguntando se quer mudar o valor ou digitar outra vez.
print('Fim do Programa')