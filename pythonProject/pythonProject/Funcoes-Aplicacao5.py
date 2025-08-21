'''O enunciado está no exercício 16.6 do módulo intermediário'''
def CalculaMedias(pNotas):
    '''Recebe o string pNotas, faz a separação dos valores, calcula e retorna a média.'''
    pNotas = pNotas.split()  #Faz as notas terem o espaço entre elas através do split(). pNotas se tornou uma lista pois o split retorna uma lista.
    for i in range(len(pNotas)):  #Para cada item vindo do comprimento de pNotas.
        pNotas[i] = float(pNotas[i])  #Faça o cada elemento sair de string para float.
    media = (pNotas[0] + pNotas[1] + pNotas[2]) * 0.3 + pNotas[3] * 0.1  #Faça as notas 1,2 e 3 tem importância de 30% e a nota 4, de 10%, depois some tudo.
    situacao = 'APROVADO' if media >= 7 else 'REPROVADO'
    pNotas.append(media) #Se coloca na lista a media através do método append
    pNotas.append(situacao) # Se coloca também a situação, aprovado ou reprovado.
    return pNotas

#PROGRAMA PRINCIPAL
notas = input('Digite 4 notas (P1, P2, P3 e NT): ')
resultado = CalculaMedias(notas) #Colocando as notas na como argumento na função

#Pega cada nota, a média e situação colocados na função e imprime na tela.
print(f'P1 = {resultado[0]:.1f}; ', end='')
print(f'P2 = {resultado[1]:.1f}; ', end='')
print(f'P3 = {resultado[2]:.1f}; ', end='')
print(f'NT = {resultado[3]:.1f} -> ', end='')
print(f'Média = {resultado[4]:.1f}; ', end='')
print(f'Situação = {resultado[5]}')
print('Fim do Programa')