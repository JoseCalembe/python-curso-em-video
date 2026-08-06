brazil=[]
estado1={'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2={'uf': 'Sao paulo', 'sigla': 'SP'}
brazil.append(estado1)
brazil.append(estado2)
print(brazil[0]['uf'])
print(brazil[0]['sigla'])
print(brazil[1]['uf'])
print(brazil[1]['sigla'])
estado=dict()
brazil=list()
for c in range(0,3):
    estado['uf']=str(input('unidade federativa: '))
    estado['sigla']=str(input('Sigla do estado: '))
    brazil.append(estado.copy())
for e in brazil:
    for v in e.values():
        print(v, end="")
    print()