ph = float(input("Digíte um valor do PH: "))
if ph < 6.0:
    r = 'ácida'
elif ph < 7.0:
    r ='levemente ácida'
elif ph == 7.0:
    r = 'neutra'
elif ph < 8.0:
    r = 'levemente alcalina'
else:
    r = 'alcalina'

print(f'Com pH = {ph} a solução é {r}')