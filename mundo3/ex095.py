galera=list()
dados=list()
totmaior=totmenor=0
for c in range(0,4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
       print(f'{p[0]} e maior de idade')
       totmaior += 1
    else:
       print(f'{p[0]} e menor de idade')
       totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')

