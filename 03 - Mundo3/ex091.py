lista=[]
while True:
    valor=int(input("Digite um valor:"))
    lista.append(valor)
    condicao=str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while condicao not in "SN":
          condicao = str(input("Quer continuar? [S/N] ")).upper()
    if condicao=="N":
       quantidade=len(lista)
       lista.sort(reverse=True)
       break
print("-="*40)
print("A lista contem {} numeros cadastrados.".format(quantidade))
print("Essa e a lista de valores ordenadas de forma decrescente: {}".format(lista))
if 5 in lista:
   cinco=lista.index(5)+1
   print("O numero 5 se encontra na posicao {} da lista dos numeros cadastrados .".format(cinco))
else:
    print("O numero 5 nao faz parte dos numeros cadastrados na lista.")