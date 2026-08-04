n=int(input("Digite um numero:"))
primeiro=0
segundo=1
cont=2
proximo=0
if n<=0:
   print("Invalido")
elif n==1:
    proximo=primeiro
    print(proximo)
else:

  print("{}  {}  ".format(primeiro, segundo), end="")
  while cont<n:
     proximo=primeiro+segundo
     primeiro=segundo
     segundo=proximo
     cont+=1
     print(proximo,end=" ")



