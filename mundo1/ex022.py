from random import shuffle
lista=[]
for c in range(1,6):
    name=str(input(f'Digite o nome do {c}◦ aluno :'))
    lista.append(name)
shuffle(lista)
print("-"*40)
print(f'{"Essa e a ordem da lista dos alunos":^30}')
print("-"*40)
for aluno in lista:
    print(aluno)
