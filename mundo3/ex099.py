matriz=[[],[],[]]
total=0
cont=0
maior=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor na posicao [{l},{c}]: ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]' , end='')
        if matriz[l][c] % 2 == 0:
           total += matriz[l][c]

    print()
print("A soma dos numeros pares e de {}".format(total))

for l in range(0,3):
    cont+=matriz[l][2]
print(f'A soma dos valores da terceira coluna  e de {cont}')
for c in range(0,3):
    if c==0:
       maior=matriz[1][c]
    elif matriz[1][c]>maior:
         maior=matriz[1][c]
print("O maior valor digitado na segunda linha foi de {}".format(maior))



