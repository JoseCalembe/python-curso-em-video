pilha=[]
frase = str(input("Digite uma frase: "))
for caracter in frase:
    if caracter=="(":
       pilha.append("(")
    elif caracter==")":
         if len(pilha)>0:
             pilha.pop()
         else:
             pilha.append(")")
             break
if len(pilha)==0:
   print("A sua expressao esta correta")
else:
    print("A sua expressao esta errada")




