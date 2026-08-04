lista=[[],[]]
for c in range(1,8):
    numero=(int(input(f'Digite o {c} numero:')))
    if numero%2==0:
       lista[0].append(numero)

    else:
       lista[1].append(numero)
pares=sorted(lista[0])
impares=sorted(lista[1])
print(f'Essa e a lista dos numeros pares {pares}')
print(f'Essa e a lista dos numeros impares {impares}')
