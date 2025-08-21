#If aninhado - um comando if dentro do outro ##

#Risco do investimento
risco = input('Digite BX ou AL para o grau de risco: ')
#Digitando o valor aqui, não impede que o programa apresente a mensagem de erro
#Tratando de não digitar nem BX ou AL
if risco != 'BX' and risco != 'AL':
    print(f'{risco} é invalido para o grau de risco !')
else:
    valor = float(input('Digite o valor: '))#Digitar o valor aqui, só é possível se o tipo de risco for válido
    if  risco == 'BX':
        if valor < 1000:
            tipo = 'Poupança'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'
    print(f'Você deve investir em: {tipo}')
