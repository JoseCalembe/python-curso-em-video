num=[1,5,7,8,4,2,5,5,10]
num[3]=6
num.append(0)
num.insert(0,12)
num.sort(reverse=True)
num.pop()
if 5 in num:
    num.remove(5)
else:
    print("Nao achei o numero 5 na lista")
print(num)
print("Essa lista tem {} elementos".format(len(num)))
valore=list()
valore.append(5)
valore.append(7)
valore.append(8)
valore.append(9)
for c,v in enumerate(valore):
    print(f'Na posicao {c} encontrei o valor {v} ! ')
for cont in range(0,5):
    valore.append(int(input(f'Digite um valor: ')))



