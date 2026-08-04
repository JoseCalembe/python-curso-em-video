dados=list()
galera=list()
maior=menor=total=0
while True:
    dados.append(str(input("Nome:")))
    dados.append(int(input("Peso:")))
    galera.append(dados[:])
    dados.clear()
    total+=1
    resp=str(input("Quer continuar? [S/N] ")).upper()[0]
    while resp not in "SN":
          resp=str(input("Quer continuar? [S/N] ")).upper()[0]
    if resp == "N":
       maior=galera[0][1]
       menor=galera[0][1]
       break
for p in galera:
    if p[1]>maior:
       maior=p[1]
    if p[1]<menor:
       menor=p[1]
print()
print("Foram cadastrados um total de {} pessoas.".format(total))
print(f'O maior peso foi de {maior}kg. peso de  ' , end='')
for p in galera:
    if p[1]==maior:
       print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg. peso de ' , end='')
for p in galera:
    if p[1]==menor:
       print(f'[{p[0]}]', end='')
