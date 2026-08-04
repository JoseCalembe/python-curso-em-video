n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
media= (n1+n2)/2
if media < 5.0:
    print("Reprovado, voce teve uma media de \033[1;31m{}\033[m ".format(media))
elif media== 5.0 or media==6.9:
    print("Voce tera que fazer o recurso por ter obtido uma media de \033[1;32m{}\033[m ".format(media))
elif media >= 7.0:
    print("Aprovado com successo, voce teve uma media de \033[1;36m{}\033[m ".format(media))