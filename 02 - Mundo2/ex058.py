soma=0
count=0
for c in range(1,7):
    num=int(input("Digite o {} valor:".format(c)))
    if num%2==0:
        soma+=num
        count+=1
print("voce digitou {} numeros pares e a soma deles e de: {}".format(count,soma))
from random import randint
