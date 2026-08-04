from random import randint

print("1 - pedra")
print("2 - papel")
print("3 - tesoura")

jogador=int(input("Escolhe uma das opcoes acima: "))


while jogador < 1 or jogador> 3:
    print("\033[1;31mJogada invalida\033[m")
    jogador=int(input("Escolhe 1,2 ou 3: "))

computador = randint(1, 3)

if computador==1:
    print("Computador escolheu pedra")
elif computador==2:
    print("Computador escolheu papel")
elif computador==3:
    print("Computador escolheu tesoura")

if jogador==computador:
    print("Empate")

elif jogador==1 and computador==2:
    print("Voce perdeu o jogo")

elif jogador==1 and computador==3:
    print("Voce venceu o jogo")

elif jogador==2 and computador==1:
    print("Voce venceu o jogo")

elif jogador==2 and computador==3:
    print("Voce perdeu o jogo")

elif jogador==3 and computador==1:
   print("Voce perdeu o jogo")

elif jogador==3 and computador==2:
    print("Voce venceu o jogo")

