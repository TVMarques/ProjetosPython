def soma(P, R, Q):
    if Q > 0:
        return P + soma(P + R, R, Q -1)
    else:
        return 0


Prim = int(input('Digite o primeiro termo: '))
Razao = int(input('Digite a razão: '))
Qtde = int(input('Digite a quantidade: '))
Resultado = soma(Prim,Razao, Qtde)
print(f'Para Prim = {Prim}; Razao = {Razao}; Qtde = {Qtde} -> Soma = {Resultado}')