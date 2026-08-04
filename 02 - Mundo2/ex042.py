nome=str(input("Qual e o seu nome:"))
if nome=="Jose":
   print("Que nome lindo!")
elif nome=="Maria" or nome=="Paulo" or nome=="Pedro":
    print("O seu nome e muito popular aqui no Brazil")
elif nome in "Ana Claudia Jessica Juliana":
    print("Belo nome feminino")
else:
    print(" Seu mome e bem normal")
print("Tenha um bom dia \033[1;36m{}\033[m".format(nome))