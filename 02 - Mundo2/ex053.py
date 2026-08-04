media=0
ano=0
menor_id=0
maior_m=0
maior_f=0
masculino=[]
feminino=[]
pessoa_n=""

for c in range(1,6):
    nome=str(input("Qual e o nome da {}ª pessoa?".format(c)))
    idade=int(input("Quantos anos tem a{}ª pessoa?".format(c)))
    sexo=str(input("De que genero e a {}ª pessoa?".format(c)))
    ano+=idade
    if c==1:
       menor_id=idade
       pessoa_n=nome

    elif menor_id>idade:
         menor_id=idade
         pessoa_n=nome

    if sexo=="masculino":
       masculino.append(idade)

       if idade>30:
          maior_m+=1

    elif sexo=="feminino":
        feminino.append(idade)

        if idade<25:
           maior_f+=1







media=ano/5
print("A media de idade do grupo e de {:.0f} anos".format(media))
print("O nome da pessoa mais nova e {}".format(pessoa_n))
print("Temos {} homens com idades maior a 30".format(maior_m))
print("Temos {} mulheres com idades inferior a 25 ".format(maior_f))
