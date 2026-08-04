salario=float(input("Digite o valor do seu salario: "))
if salario<=1250:
    aumento=salario+(salario*15/100)
    print("Com o aumento de 15%, o teu salario sera {:.2f}".format(aumento))
else:
    aumento=salario+(salario*10/100)
    print("Com o aumento de 10%, o teu salario sera {:.2f}".format(aumento))
