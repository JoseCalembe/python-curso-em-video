import math
angulo=float(input("Digite um angulo qualquer:"))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tagente=math.tan(math.radians(angulo))
print("O seno de {} e {:.2f}".format(angulo,seno))
print("O cosseno de {} e {:.2f}".format(angulo,cosseno))
print("A tangente de {} e {:.2f}".format(angulo,tagente))

