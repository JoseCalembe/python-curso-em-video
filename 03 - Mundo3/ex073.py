n=0
soma=0
cont=0
while True:
    n=int(input("Digite um numero: "))
    if n == 999:
       break
    cont += 1
    soma += n

print("Foram digitados {} numeros no total".format(cont))
print("A soma entre os numeros digitados e de {}".format(soma))