from random import randint
cont=0
while True:
    print("Vou pensar em um numero entre 0 e 20, tente adivinhar...")
    computador = randint(0, 20)
    jogador=int(input("Em que numero pensei? "))
    print("Pensei no numero {}".format(computador))
    cont += 1

    if jogador==computador:
       if cont==0:
          print("Voce venceu na primeira tentativa")
       else:
           print("Voce venceu depois de {} tentativas".format(cont))
       break
    else:
        print("Opcao errada!")
        condicao=str(input("Queres tentar novamente: [S/N]")).upper()
        while condicao not in "SsNn":
              condicao = str(input("Queres tentar novamente: [S/N]")).upper()
              if condicao=="N":
                 break
print("Fim do jogo")