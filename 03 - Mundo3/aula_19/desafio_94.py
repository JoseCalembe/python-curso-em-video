lista=list()
dados=dict()
cont=0
media=0
soma_ida=0
while True:
    dados['Nome']=(input('Nome: '))
    dados['Sexo']=(input('Sexo [M/F]: ')).upper().strip()[0]
    dados['Idade']=int(input('Idade: '))
    soma_ida+=dados['Idade']
    lista.append(dados.copy())
    cont+=1
    dados.clear()
    resp=input("Quer continuar? [S/N]").strip().upper()[0]
    while resp not in 'SN':
        resp=input("Quer continuar? [S/N]").strip().upper()[0]
    if resp=="N":
       media=(soma_ida/cont)
       break
print(f'Foram cadastradas um total de {cont} pessoas')
print("A media da idade do grupo e de {:.0f} anos ".format(media))
print(f'As mulheres cadastradas foram: ',end=' ')
for dados in lista:
    if dados['Sexo']=='F':
       print(f'{dados["Nome"]} ' ,  end=' ')
print()
print("Lista das pessoas que estao acima da media:")
for dados in lista:
    if dados['Idade']>media:
        print(f'Nome = {dados["Nome"]}; Sexo = {dados["Sexo"]}; Idade = {dados["Idade"]}')
print("<<<ENCERRADO>>>")
