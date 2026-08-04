velo=int(input('Qual a quantidade de velocidade em km/h? '))
if velo>80:
    excesso= velo-80
    multa= excesso*7.00
    print("Voce foi multado por exceder {} Km do limite da velocidade".format(excesso))
    print("A multa sera de R$ 7.00 por cada Km")
    print("Como voce estava a dirigir com uma velocidade de {} Km, voce pagara uma multa de R$ {:.2f}".format(velo,multa))
else:
    print("voce esta dentro do limite velocidade")