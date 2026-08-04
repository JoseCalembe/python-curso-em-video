import math
cateto_oposto=float(input("digite o comprimento do cateto oposto:"))
cateto_adjacente=float(input("digite o comprimento do cateto adjacente:"))
Hipotenusa=math.sqrt(cateto_oposto**2+cateto_adjacente**2)
print("O comprimento da hipotenusa e de: {}cm".format(math.ceil(Hipotenusa)))