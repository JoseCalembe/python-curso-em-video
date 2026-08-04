frase=str(input("Digite uma frase:"))
replace=frase.replace(" ","")
for c in range(len(replace) -1, -1, -1):
    print(replace[c], end="")
print()
if frase== frase[::-1]:
    print("A frase digitada e um palindromo")
else:
    print("A frae digiada nao e um palindromo")

