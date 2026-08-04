from random import randint
print("-=-" * 20)
print("Vamos jogar par ou impar")
print("-=-" * 20)
cont=0
while True:
    computador = randint(1, 1000)
    usuario=int(input("Diga um valor:"))
    jogo=str(input("Par ou impar [P/I]")).upper().strip()
    soma=usuario+computador
    if jogo == "P" and soma % 2 == 0:
        cont+=1
        print("Voce jogou {} e o computador {} a soma e de {} deu par".format(usuario, computador, soma))
        print("Voce venceu!")
        print("Jogar novamente....")


    elif jogo == "I" and soma % 2 != 0:
        cont += 1
        print("Voce jogou {} e o computador {} a soma e de {} deu impar".format(usuario, computador, soma))
        print("Voce venceu!")
        print("Jogar novamente....")


    elif jogo == "P" and soma % 2 != 0:
        print("Voce jogou {} e o computador {} a soma e de {} deu impar".format(usuario, computador, soma))
        print("Voce perdeu!")
        break

    elif jogo == "I" and soma % 2 == 0:
        print("Voce jogou {} e o computador {} a soma e de {} deu par".format(usuario, computador, soma))
        print("Voce perdeu!")
        break
print("Fim do jogo")
print("Voce venceu {} vezes consecutivas".format(cont))



