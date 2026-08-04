valor=int(input("Digite um montante que deseja sacar: "))
primeiro=0
segundo=0
terceiro=0
quarto=0
while valor> 0:

    if valor>=50:
       valor-=50
       primeiro+=1

    if valor<50 and valor>=20:
        valor-=20
        segundo+=1

    if valor<20 and valor>=10:
        valor-=10
        terceiro+=1

    if valor<10 and valor>0:
        valor-=1
        quarto+=1

if primeiro>0:
   print("Total de {} notas de 50".format(primeiro))

if segundo>0:
    print("Total de {} notas de 20".format(segundo))

if terceiro>0:
    print("Total de {} notas de 10".format(terceiro))

if quarto>0:
    print("Total de {} notas de 1".format(quarto))


