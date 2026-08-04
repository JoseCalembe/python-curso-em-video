from datetime import datetime
data=int(input("Digite a data de nascimento: "))
anoactual=datetime.now().year
idade=anoactual-data
limite=18
if idade<limite:
   tempo_restante=limite-idade
   print("Como voce tem apenas {} anos de idade e o limite para o recrutamento e de {} anos ".format(idade,limite))
   print("Voce podera se cadastrar para o recrutamento em {} anos".format(tempo_restante))

elif idade>limite:
     tempo_passado=idade-limite
     print("Como voce tem {} anos de idade e o limite para o recrutamento e de {} anos ".format(idade, limite))
     print("Voce nao podera se cadastrar para o recrutamento pelo facto de terem passado {} anos, para o recrutamento de cidadoes da sua idade".format(tempo_passado))
else:
    print("Como voce tem {} anos de idade e o limite para o cadastro e de {} anos, esse e o momento certo para fazeres o seu cadastro".format(idade,limite))



