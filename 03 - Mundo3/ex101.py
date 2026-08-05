lista=list()
dados=list()
while True:
    dados.append(str(input("Nome:")))
    dados.append(int(input("Nota 1 :")))
    dados.append(int(input("Nota 2 :")))
    media=(dados[1]+dados[2])/2
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    resp=str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while resp not in "SN":
        resp=str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp=="N":
       break
print("-"*30)
print(" No.   NOME     MEDIA")
print("-"*30)
for i,v in enumerate(lista):
    print(f'{i}    {v[0]}     {v[-1]}')
while True:
    notas=int(input("Monstrar notas de qual aluno?  (999 interrompe) "))
    if notas==999:
        break
    elif 0<=notas<len(lista):
         print(f'As notas do/a {lista[notas][0]}: {lista[notas][1]} e {lista[notas][2]}')

    else:
        print(f'O aluno No {notas} nao faz parte da lista dos alunos cadastrados!')