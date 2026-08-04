r1=int(input("Digite o comprimento da primeira reta:"))
r2=int(input("Digite o comprimento da segunda reta:"))
r3=int(input("Digite o comprimento da terceira reta:"))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
   print("As tres retas podem formar um triuangulo!")
   if r1==r2==r3:
       print("As retas formam um triangulo equilatero")
   elif r1==r2 or r1==r3 or r2==r3:
       print("As tres retas formam um triangulo Isosceles")
   else:
       print("As tres retas formam um triangulo Escaleno")
else:
    print("As tres retas nao formam um triangulo")
