def funcao1():
    print('dentro da função1 temos >>', a, b)#Aqui são utilizados objetos de escopo global

def funcao2():
    #Abaixo os objetos de escopo local - Definidos dentro da função. Não se esqueça que a preferência de uso é de objetos locais.
    a = 100
    b = 200
    print('dentro da função2 temos >>', a, b)

# parte principal - aqui se define o escopo global. Nunca define objetos locais com o mesmo nome que as globais, por conveniência.
a = 10
b = 20

funcao1()
funcao2()
print('Fora das funções temos  >>', a, b)
