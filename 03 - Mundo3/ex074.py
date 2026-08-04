usuario= 0

while True:
    usuario= int(input("Quer ver a tabuada de que valor?: "))

    if usuario<=0:
        break
    for c in range(1, 13):
        print(f'{usuario}x{c} = {usuario * c}')
print("FIM")