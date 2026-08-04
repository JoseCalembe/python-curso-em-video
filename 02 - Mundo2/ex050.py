peso=float(input("Digite o seu peso:"))
altura=float(input("Digite sua altura:"))
imc=peso/(altura**2)
if imc<18.5:
    print("Voce esta abaixo do peso")
elif imc>=18.5 and imc<25:
    print("Voce esta no peso ideal")
elif imc>=25 and imc<30:
    print("Voce esta no sobrepeso")
elif imc>=30 and imc<40:
    print("Voce esta na obesidade")
else:
    print("Voce esta sob obesidade morbida")