n=int(input("Digite um numero: "))
cont=0
soma=0
mais=0
while n!=999:
    cont += 1
    soma+=n
    n=int(input("Digite um numero: "))
print("Foram digitados {} numeros no total".format(cont))
print("A soma entre os numeros digitados e de {}".format(soma))


