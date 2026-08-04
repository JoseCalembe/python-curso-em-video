lista=[]
while True:
     valor=int(input("digite um valor: "))

     if valor not in lista:
        lista.append(valor)
        print("Valor adiciondo com sucesso...")
     else:
        print("Valor duplicado! Nao vou adicionar...")
     condicao = str(input("deseja continuar? [S/N]")).upper()
     while condicao not in "SsNn":
           condicao = str(input("deseja continuar? [S/N]")).upper()
     if condicao=="N":
        lista.sort()
        break
print("Essa e a lista dos valores digitados:{} ".format(lista))
print("fim")











