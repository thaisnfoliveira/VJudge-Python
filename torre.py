t = int(input())
cont = 0

def movimentos(letra, digito):
    colunas = ["a", "b", "c", "d", "e", "f", "g", "h"]
    linhas = ['1', '2', '3', '4', '5', '6', '7', '8']
    movimentos = []

    linhas.remove(digito)

    for i in linhas:
        movimentos.append(letra+i)
    
    colunas.remove(letra)

    for j in colunas:
        movimentos.append(j+digito)

    apresentacao = ""
    
    for k in movimentos:
        apresentacao+= k+"\n"
    
    apresentacao = apresentacao.strip()
    print(apresentacao)


while cont<t:
    casoTeste = input()
    letra = casoTeste[0]
    digito = casoTeste[1]

    movimentos(letra, digito)
    cont+= 1
