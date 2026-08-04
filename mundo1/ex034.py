v=float(input("quantos Km foi percorrido ao longo da viagem?: "))
if v<=200:
    preco=(v*0.50)
else:
    preco=(v*0.45)
print("O valor a pagar pela viagem e de R${:.2f}".format(preco))

