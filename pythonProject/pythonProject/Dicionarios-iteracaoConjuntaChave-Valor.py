cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário  -  Caso 3')
for item in cores.items():#for numero, cor in cores.items():   ---> outra forma de fazer colocando a tupla do iterador for.
    # Obs: deve-se colocar isso no print se for a outra forma do 'for' == print(f' n° da cor = {numero} - nome da cor = {cor}')
    print(f' n° da cor = {item[0]} - nome da cor = {item[1]}')#Assim o imprimir na tela será com o número e o nome da cor, pois isso é ma tupla.
print('\nFim do Programa')