num=int(input("Digite um  numero: "))
c=num
f=1
print("Calculando {}!".format(c))
while c>0:
    print("{}".format(c),end="")
    print("x" if c>1 else "=",end="")
    f*=c
    c-=1
print(f)


