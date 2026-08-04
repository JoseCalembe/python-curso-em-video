import random
lista=[]
for c in range(1,5):
    name=str(input(f'Digite o nome do {c}◦ aluno :'))
    lista.append(name)
escolhido=random.choice(lista)
print("o escolhido foi {}".format(escolhido))