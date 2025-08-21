Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print('Alternativa com if clássico')
for codigo in Codigos:
    if 120 <= codigo and codigo <= 200:
        Lista.append(codigo)
print(f' códigos filtrados --> {Lista}')

Lista = []
print('\n\nAlternativa com if inline')
for codigo in Codigos:
    Lista.append(codigo) if 120 <= codigo and codigo <= 200 else 0
print(f' códigos filtrados de outra maneira --> {Lista}')