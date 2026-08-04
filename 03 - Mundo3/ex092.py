lista=[]
pares=[]
impares=[]
while True:
    valore=int(input("Digite um numero inteiro: "))
    if valore in lista:
        print("Esse numero ja se encontra na lista nao vou adicionar")
    else:
        lista.append(valore)
    resp=str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while resp not in "SN":
          resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
       for v in lista:
           if v % 2 == 0:
              pares.append(v)
           else:
              impares.append(v)
       break
print("-="*30)
print("A lista dos valores digitados foi {}".format(lista))
print("A lista dos valores pares digitados foi {}".format(pares))
print("A lista dos valores impares digitados foi {}".format(impares))



