primeiro=int(input("Primeiro termo: "))
razao=int(input("Razao:"))
termo=primeiro
cont=1
mais=10
total=0
while mais != 0:
    total=total+mais
    while cont<=total:
        print("{} -> ".format(termo),end="")
        termo=termo+razao
        cont+=1
    print("PAUSA")
    mais=int(input("Quantos termos deseja mostrar a mais: "))
print("FIM DO PROGRAMA")
print("A progressao foi finalizada com {} termos".format(total))



