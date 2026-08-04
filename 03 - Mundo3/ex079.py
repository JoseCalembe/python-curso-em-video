lanche = ("Hanburguer" , "Suco" , "Pizza" , "Pudim", "Batata frita")
print(lanche)
print(sorted(lanche))
#for comida in lanche:
    #print("Eu vou comer {}".format(comida))
#print("Comi pra caramba!")

#for  cont in range(0, len(lanche)):
     #print(f"Vou comer {lanche[cont]}")

for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posicao {pos}")

for cont in range(0, len(lanche)):
    print(f"Vou comer {lanche[cont]} na posicao {cont}")