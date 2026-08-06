pessoas={'nome': 'Jose', 'sexo': 'M', 'idade': 23}
pessoas['peso']=100
pessoas['nome']='Calembe'
del pessoas['sexo']
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k,v in pessoas.items():
    print(f'{k} = {v}')