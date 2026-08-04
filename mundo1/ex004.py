soma=0
for m in range(1,4):
    nota=float(input("Digite a {}ª nota: ".format(m)))
    soma +=nota
media=soma/3
if media >=5:
    print("Voce teve uma media de {:.2f} valores, parabens passaste de fase".format(media))
else:
    print("Voce teve uma media de {:.2f} valores, infelizmente nao poderas passar de fase".format(media))




