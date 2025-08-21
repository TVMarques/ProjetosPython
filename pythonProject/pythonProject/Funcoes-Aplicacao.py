'''Enunciado
Escreva função que recebe um número inteiro como parâmetro de entrada e retorna
o texto "PAR" ou "ÍMPAR". Use-a em um programa principal '''

def Paridade(a):
    return 'PAR' if a % 2 == 0 else 'ÍMPAR' #Esta forma é a if inline, com o mesmo comportamento dos comandos abaíxo.
    #if a % 2 == 0:
        #return 'PAR'
   # else:
       # return 'ÍMPAR

#Parte principal
n = int(input('Digite um inteiro: '))
print(Paridade(n))