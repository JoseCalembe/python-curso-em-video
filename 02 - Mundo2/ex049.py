r1=float(input("Digite o comprimento da primeira reta: "))
r2=float(input("Digite o comprimento da segunda reta: "))
r3=float(input("Digite o comprimento da terceira reta: "))
if (r1<r2+r3) and (r2<r1+r3) and (r3<r1+r2):
    print("As 3 retas formam um triangulo")

    if (r1==r2 and r2==r3):
         print("As 3 retas formam um triangulo equilatero")
    elif (r1==r2 or r2==r3 or r3==r1):
         print("As 3 retas formam um triangulo isosceles ")
    else:
         print("As 3 retas formam um triangulo escaleno")
else:
   print("As 3 retas nao formam um triangulo")
