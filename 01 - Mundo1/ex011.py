real=float(input("quanto dinheiro voce tem na carteira?"))
dolar=real/3.27
euro=real/5.45
print("com R${} voce pode comprar {:.2f} EUR".format(real,euro))
print("com R${} Voce pode comprar {:.2f} US$ ".format(real,dolar))