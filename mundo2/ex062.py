from datetime import date
actual=date.today().year
totmaior=0
totmenor=0
for pess in range(1,8):
    nasc=int(input("Qual e o ano de nascimento da {}ª pessoa".format(pess)))
    idade=actual-nasc
    if idade>=21:
        totmaior +=1
    else:
        totmenor +=1
print("Temos um total de {} pessoas maiores de idade".format(totmaior))
print("Temos tambem um total de {} pessoas menores de idade".format(totmenor))

