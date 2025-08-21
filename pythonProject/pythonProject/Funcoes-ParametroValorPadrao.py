def Saudacao(nome, mensagem = 'Olá'):
    print(mensagem, nome)

Saudacao('José', 'Bom dia')#O "Olá" do parâmetro mensagem, será ignorado pois foi sobreescrito.
Saudacao('José')#Assim, mensagem terá o seu valor padrão, que é "Olá".
