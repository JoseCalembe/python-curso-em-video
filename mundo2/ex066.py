count=0
from random import randint
from time import sleep
computador=randint(0,2)
print("-=-"*20)
print("Vou pensar em um numero entre 0 e 10, tente advinhar...")
print("-=-"*20)
jogador=int(input("Em que numero eu pensei?"))
print("PROCESSANDO...")
sleep(2)
while jogador!=computador:
      count+=1
      jogador = int(input("opcao invalida, tente novamente:"))
      print("PROCESSANDO...")
      sleep(2)
print("Parabens, voce venceu mas precizou de {} tentativas para vencer o jogo".format(count))
