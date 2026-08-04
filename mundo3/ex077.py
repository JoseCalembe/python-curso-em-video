total=0
caro=0
cont=0
barato=0
produto=""
while True:
    nome=str(input("Qual e o nome do produto: "))
    preco=float(input("Qual e o valor do produto: "))
    total+=preco
    cont+=1
    if cont == 1:
        barato = preco
        produto = nome

    elif preco< barato:
        barato = preco
        produto = nome

    if preco>1000:
       caro+=1
    mais=str(input("Quer continuar?[S/N] ")).upper().strip()

    while mais not in "SN":
        mais= str(input("Quer continuar? [S/N] ")).upper().strip()


    if mais == "N":
        break
print("-="*20)
print("Gastou-se um total de {} R$ para a aquisicao dos produtos".format(total))
print("Temos {} produtos com um preco acima de 1000 R$".format(caro))
print("O nome do produto mais barato que temos e {} que custa {}".format(produto,barato))
print("E temos um total de {} produtos cadastrados".format(cont))

