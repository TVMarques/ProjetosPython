'''Enunciado
Escreva um programa que verifique se um número inteiro é primo.
Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.
A verificaçãoo do primo deve ser feita dentro de uma função.'''

def Primo(V):
    '''Se V for primo retorna true, senão retorna false'''
    # Verificando os números pares
    if V == 2:  # 2 é o primeiro número par primo, então se V  for igual a 2, haverá um retorno True
        return  True
    elif V % 2 == 0:  #Os outros números pares retornam false e não são primos
        return False
    else: #Verificando velozmente se os números ímpares são primos
        raiz = pow(V, 0.5) #a raiz quadrada de V
        i = 3
        while i <= raiz: #Enquanto i for menor/igual que raiz de V, faça: . (Se faz isso para verificar se o resto torna o número primo ou não, economizando operações aritiméticas)
            if V % i == 0: #Se o resto da divisão de V por i for 0, então não é primo
                return  False
            i += 2 #O i avança de 2 em 2 começando em 3.
        return True #Isto indica que o número é primo se no laço o valor i tiver o resto DIFERENTE de 0.

N = int(input('Digite um inteiro: '))
if Primo(N):
    print(f'{N} é primo')
else:
    print(f'{N} não é primo')