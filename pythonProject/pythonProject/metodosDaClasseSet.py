c1 = {16, 21, 8, 31, 41, 28, '8'} #Criando conjuntos no qual, não é permitido repetir o objeto. Os objetos podem ser de qualquer tipo.

print(c1)

c2 = set((6655,24,'Thiago'))#Construtor dos conjuntos o set(), criando conjunto vazio. Pode-se adicionar vários elementos como se fosse um, através de uma tupla () ou lista []
c2.add(234)#Adicionando um elemento na classe. O add serve para isso.

c3 = set([7, 78, 'Bom'])

print(type(c2))

print(c2)

print(c3)


#c3.clear() #O clear limpa o conjunto

d = c1.copy()  # Copiando o conjunto c1 no objeto d, que terá o id diferente.
print(id(c1))
print(id(d))

d2 = set(c2) #Outra forma de fazer a cópia de um conjunto.
print(d2, id(d2))
print(c2, id(c2))

c4 = {17, 19, 25, 36, 44, 58, 63}
c5 = {19, 20, 22, 33, 44, 58, 60}
print(c4.difference(c5))# O difference, traz todos os elementos que estão no c4 e NÃO estão no c5.

#c4.difference_update(c5) #Assim a diferença do que existe em c5 será colocada em c4.
#print(c4)

c1.discard('8')#Este comando remmove um elemento. Se não existir o elemento, não acontece nada.
print(c1)

e = c4.intersection(c5) #O intersection retorna os elementos iguais nos dois conjuntos. Pode ser atribuido a outro objeto.
print(e)

#c4.intersection_update(c5)# O c4 é alterado para ter somente o resultado da interseção
#print(c4)

#print(c4.isdisjoint(c5))#Determina se os elementos que estão em c4 são diferentes do de c5.
#c4.discard(58)
#c4.discard(19)
#c4.discard(44)
#print(c4.isdisjoint(c5))#Agora deu true.



'''print(c4.issubset(c5))# Verificando se os elementos em c4 estão em c5 como subconjunto. Se todos os elementos de c4 forem os de c5.
c4.discard(17)
c4.discard(36)
c4.discard(25)
c4.discard(63)
print(c4)
print(c5)
print(c4.issubset(c5))#Assim deu True.

print(c4.issuperset(c5)) #Retorna se c5 faz parte do c4 como superconjunto, dará falso.
print(c5.issuperset(c4)) #Retorna se c4 faz parte do c5 como superconjunto, dará verdaddeiro.'''

'''print(c3)
ex = c3.pop()#Exclui um elemento escolhido pelo método, no conjunto.
print(c3)
ex = c3.pop()
print(c3)
ex = c3.pop()
print(c3)
ex = c3.pop() #Ficou vázio, assim dará um erro pois não é permitido fazer a operação.
print(c3)'''

'''print(c2)
c2.remove(6655)#Removendo um elemento de c2.
print(c2)
c2.remove(44)# Se usar um remove, sem que haja o elemento no conjunto, haverá erro.'''
#print(44 in c2)# Perguntando se existe o elemento 44 em c2, para assim fazer o .remove. Dará false


print(c4)
print(c5)
d3 = c4.union(c5) #Unindo os elementos de c4 e c5, que não repetirá por regra os elemntos iguais entre si.
print(d3)
print(f'{len(c4)} elementos')
print(f'{len(c5)} elementos')
print(f'{len(d3)} elementos')

print(f'{e} elementos iguais de c4 e c5')
print(c4.symmetric_difference(c5))#A diferença assimétrica é todos os elementos unidos de c4 e c5, menos os que são iguais entre eles.


print(c4.union(c5)) #O union atualiza o c4 com a união do c5.
print(f'c4 = {c4}')