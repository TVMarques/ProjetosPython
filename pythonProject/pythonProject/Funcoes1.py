def ExibeHifens():
    print('------')#Usando função

#Parte principal
lista = [10, 20, 30, 40]
for item in lista:
    print(item)
    ExibeHifens()

lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
for item in lista2:
    print(item)
    ExibeHifens()

print('Fim do Programa')