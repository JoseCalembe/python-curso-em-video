numero=int(input("Digite um numero inteiro:"))
print("Tabuada de {}:".format(numero))
for c in range(1,13):
    print(f'{numero} x {c} = {numero*c}')