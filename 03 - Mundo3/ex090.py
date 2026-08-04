lista=[]
for c in range(1,6):
     valor=int(input(f'Digite o {c} valor: '))
     if len(lista)==0 or valor>lista[-1]:
         lista.append(valor)
         print("Valor addicionado no final da lista")
     else:
         for posicao in range(len(lista)):
             if valor<=lista[posicao]:
                lista.insert(posicao,valor)
                print(f'Valor addicionado na posicao {posicao} da lista')
                break
print("-"*40)
print("Essa e a ordem da lista dos numeros digitados: {}".format(lista))