num=(int(input("Digite um numero de 0 a 10:")),
      int(input("Digite um numero de 0 a 10:")),
      int(input("Digite um numero de 0 a 10:")),
      int(input("Digite um numero de 0 a 10:")))

pare=0
print("Voce digitou os seguintes valores: {}".format(num))
if 9 in num:
    cont=num.count(9)
    print("O numero 9 apareceu {} vezes".format(cont))
if 3 in num:
    posicao = num.index(3)
    mais = posicao+1
    print("O numero 3 apareceu na {} posicao".format(mais))
else:
    print("O numero 3 nao foi digitado na lista")
print("Esses foram o numeros pares encontrados:" , end=' ')
for n in num:
    if n%2==0:
       print(n,end=' ')
