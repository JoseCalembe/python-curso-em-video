from datetime import datetime
data=int(input("Digite  sua data de nascimento: "))
anoactual=datetime.now().year
idade=anoactual-data
if idade<=9:
   print("Como voce tem {} anos de idade, pertences a categoria mirin".format(idade))
elif idade<=14:
     print("Como voce tem {} anos de idade, pertences a categoria infantil".format(idade))
elif idade<=19:
     print("Como voce tem {} anos de idade, pertences a categoria junior".format(idade))
elif idade<=24:
     print("Como voce tem {} anos de idade, pertences a categoria senior".format(idade))
else:
    print("Como voce tem {} anos de idade, pertences  categoria Master".format(idade))