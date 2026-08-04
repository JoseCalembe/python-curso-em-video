n=int(input("Digite um numero inteiro:"))
usuario=str(input("Ainda pretendes continuar?"))
media=0
menor=n
maior=n
total=n
cont=1
while  usuario == "sim":
    n = int(input("Digite um numero inteiro:"))
    usuario = str(input("Ainda pretendes continuar?"))

    total+=n
    cont+=1
    media=total/cont

    if n> maior:
       maior=n

    if n< menor:
       menor=n
print("A media entre os numeros digitados e de {:.2f}".format(media))
print("O maior numero digitado foi {}".format(maior))
print("O menor numero digitado foi {}".format(menor))





