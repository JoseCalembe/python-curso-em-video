pessoa = ""
media=0
ano=0
maior_m=0
menor_f=0
masculino=[]
feminino=[]

for n in range(1,5):
    nome=str(input("Qual e o nome da {}ª pessoa:".format(n)))
    idade=int(input("Qual e a idade da {}ª pessoa:".format(n)))
    sexo=str(input("Qual e o genero da {}ª pessoa:".format(n)))

    ano+=idade
    if sexo=="masculino":
       masculino.append(idade)

       if len(masculino)==1:
           maior_m=idade
           pessoa=nome
       elif idade<maior_m:
            maior_m=idade
            pessoa=nome

    else:
        feminino.append(idade)

        if idade<20:
           menor_f+=1
media=ano/4




print("Numero de pessoas do genero masculino", len(masculino))
print("Numero de pessoas do genero feminino",len(feminino))
print("A media de idade do grupo e de: {:.0f} anos".format(media))
print("O homen mais velho tem {} anos de idade".format(maior_m))
print("O nome do homem mais velho e {}".format(pessoa))
print("{} mulheres tem menos de 20 anos".format(menor_f))

