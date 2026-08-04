lista=[]
for c in range(1,6):
    valores=int(input(f'Digite o {c}◦ numero: '))
    lista.append(valores)
maior=max(lista)
menor=min(lista)
print("Essa e a lista de numeros gerados: {}".format(lista))
print(f'O maior numero digitado foi {maior} e o mesmo aparece na '  ,end="")
for pos,v in enumerate(lista):
    if v==maior:
       print(f'{pos+1}◦...' ,end="")
print("posicao")
print(f'O menor numero digitado foi {menor} e o mesmo aparece na ' ,end="")
for pos,v in enumerate(lista):
    if v==menor:
       print(f'{pos+1}◦...' , end="")
print("posicao")
