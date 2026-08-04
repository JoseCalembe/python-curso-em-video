frase=input("Digite uma frase: ").lower()
letras=len(frase.replace(" ",""))
todo=(frase.replace(" ",""))
if "a" in frase:
   quantidade_a=todo.count("a")
   primeira_posicao = todo.find("a")+1
   ultima_posicao = todo.rfind("a")+1
   print("A letra a aparece {} vezes na frase".format(quantidade_a))
   print("A primeira letra a aparece na {} posicao".format(primeira_posicao))
   print("A ultima letra a aparece na {} posicao".format(ultima_posicao))
else:
    print("A letra a nao aparece na frase")
print("A frase tem no eu todo {} letras".format(letras))

