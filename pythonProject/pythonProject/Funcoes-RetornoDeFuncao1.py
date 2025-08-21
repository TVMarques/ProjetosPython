def LerInteiro():
    n = int(input('Digite um inteiro: '))
    return n#Se não colocar o return o retorno da função será a classe none

#Parte principal
valor = LerInteiro()#Este é o uso do retorno da função
print(f'O valor lido na função foi = {valor}')