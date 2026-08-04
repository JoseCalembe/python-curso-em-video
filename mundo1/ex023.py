name=str(input("Digite o seu nome completo: "))
print("-"*40)
todo=name.split()
if len(todo)>1:
   segundo_nome= todo[1]
   print("O seu segungo nome e {}, e o mesmo tem {} letras".format(segundo_nome, len(segundo_nome)))
else:
    print("O seu nome completo contem apenas um nome,nao existe um segundo nome")
print("O seu nome em maisculas e: {}".format(name.upper()))
print("O seu nome em minusculas e:{}".format(name.lower()))
print("O seu nome no seu todo tem {} letras".format(len(name)-name.count(' ')))
