from random import randint
lista = list()
jogos=list()
quant=int(input('Quantos jogos deseja sortear: '))
tot=1
while tot<=quant:
    cont = 0

    while True:
        numero=randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont+=1
        if cont==6:
            break
    lista.sort()
    jogos.append(lista[:])
    tot+=1
    lista.clear()
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')