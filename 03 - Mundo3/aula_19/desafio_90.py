lista=dict()
lista['nome']=str(input('Nome:'))
lista['media']=float(input(f'Media de {lista['nome']}:'))
if lista['media'] >= 7:
    lista['situacao']='Aprovado'
else:
    lista['situacao']='Reprovado'
print(f'Nome e igual a {lista["nome"]}')
print(f'Media e igual a {lista["media"]}')
print(f'Situacao e igual a {lista["situacao"]}')