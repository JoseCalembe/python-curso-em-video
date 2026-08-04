lista=[]
for c in range(1,7):
    lista.append(int(input(f'Digite o {c} numero:')))
maior=max(lista)
menor=min(lista)
print(f'O maior numero digitado foi {maior}, nas seguintes posicoes: ' , end=' ')
for pos,v in enumerate(lista):
    if v==maior:
       print(f'{pos+1}' , end=" ")
print()
print(f'O menor numero digitado foi {menor}, nas seguintes posicoes: '  ,  end=' ')
for pos,v in enumerate(lista):
    if v==menor:
       print(f'{pos+1}'  , end=" ")