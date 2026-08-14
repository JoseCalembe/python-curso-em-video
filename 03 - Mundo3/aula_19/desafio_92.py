from datetime import datetime
trabalhador=dict()
dataactual=datetime.now().year
trabalhador['nome']=(input('Nome:'))
ano=int(input('Ano de Nascimento:'))
trabalhador['idade'] = dataactual - ano
trabalhador['ctps']=int(input('Carteira de trabalho (0 nao tem):'))
if trabalhador['ctps']==0:
   print("-"*40)
   print(trabalhador)

else:
    trabalhador['contratacao']=int(input('Ano de contratacao:'))
    trabalhador['salario']=float(input('Salario: R$'))
    aps=trabalhador['contratacao']-ano
    trabalhador['aposentadoria']=aps+35
    print("-"*50)
    print(trabalhador)
for k,v in trabalhador.items():
    print(f'{k} tem o valor {v}')