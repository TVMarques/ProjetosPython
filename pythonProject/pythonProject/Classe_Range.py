'''Enunciado
Usando a classe range, escreva um programa que leia três números inteiros:
o primeiro termo P, a razão R e a quantidade Q de termos de uma progressão aritimética. O programa deve
calcular os Q termos da progrssão colocando-os em uma lista e no final exibi-la na tela.'''

P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
Q = int(input('Digite a quantidade de termos: '))

ultimo = P + R * (Q - 1)
Termos = list(range(P, ultimo+1 ,R))

print("\nLista gerada com range:")
print(Termos)
print('Fim do programa')