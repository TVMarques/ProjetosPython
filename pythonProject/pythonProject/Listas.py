l = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print('Exibição da lista completa')
print(l)#Manipulação como um todo da lista
print('\nExibição dos elementos individuais')
i = 0
while i < len(l):
    print(l[i], end='   ')#Manipulação linha a linha da lista com separação de três espaços e sem vírgula.
    i  = i + 1
print('\nFim do programa')


'''from threading import *

import time

s = Semaphore(2)


def example(nome, idade):
    for i in range(3):
        s.acquire()

        print("Olá", nome, idade)

        time.sleep(2)

        s.release()


threadA = Thread(target=example, args=("João", 15))

threadB = Thread(target=example, args=("José", 20))

threadC = Thread(target=example, args=("Maria", 26))

threadD = Thread(target=example, args=("Ana", 29))

threadA.start()

threadB.start()

threadC.start()

threadD.start()'''