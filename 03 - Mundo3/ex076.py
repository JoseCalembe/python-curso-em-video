pessoas=0
homens=0
mulheres=0


while True:
    print("CADASTRE UMA PESSOA")
    idade=int(input("Informe sua idade:"))
    sexo=str(input("Sexo: [M/F]")).upper().strip()

    while sexo not in "MF":
          sexo = str(input("Sexo: [M/F]").upper().strip())
    mais=str(input("Ainda qures continuar [S/N]:")).upper().strip()

    while mais not in "SN":
          mais=str(input("Ainda qures continuar [S/N]")).upper().strip()
    if sexo=="M":
       homens+=1

    if sexo=="F" and idade<20:
       mulheres+=1

    if idade > 18:
        pessoas += 1

    if mais == "N":
       break

print("{} Pessoas tem mais de 18 anos.".format(pessoas))
print("Foram cadastrados um total de {} homens  ".format(homens))
print("{} mulheres tem menor de 20 anos".format(mulheres))
print("Fim do programa....")


