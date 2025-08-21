'''A função tem como objetivo receber na entrada um número inteiro, depois transformar esse número
em string para se poder iterar sobre cada elemento do número. Adiante, pega-se cada dígito iterado e multiplica cada
um por um peso que começa de 2 e vai a 6, com os valores da multiplicação sendo somados tendo a soma sendo dividida por 7.
Assim se obtém o digito verificador.
EX: 31483, esse número é trasnsformado em string e cada um desses números são multiplicados pelo peso que começa de 2 e vai
a 6, depois, somando as múltiplicações, se obterá o resultaado 83, com ele sendo dividido por 7 o resto será 6.'''
def CalcDigito(cod):
    s = str(cod)#Primeiro, transforma o código trasferido como parâmetro em string.
    peso = 2
    dv = 0
    for a in s:
        dv += peso * int(a)  # A cada repetição, se multiplica o valor de a, que é cada elemento vindo do código, * o peso
        peso += 1  # E se acrescenta um em peso
        return  dv % 7 #Daqui se terá o digito verificador

codigo = int(input('Digite o código: '))
while codigo > 0:
    digito = CalcDigito(codigo)
    print(f'Código: {codigo} --> dígito: {digito}')
    codigo = int(input('Digite o código: '))

print('Fim do Programa')
