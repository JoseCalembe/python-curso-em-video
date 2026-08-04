n1=int(input("Primeiro numero:"))
n2=int(input("Segundo numero:"))
opcao=0
while opcao!=5:
    print(" [1] Somar")
    print(" [2] Multiplicar")
    print(" [3] Maior")
    print(" [4] Novos numeros")
    print(" [5] Sair do programa")
    opcao = int(input("Qual a opcao:"))
    if opcao==1:
       soma=n1+n2
       print("A soma entre {} e {} e igual a {}".format(n1,n2,soma))
    elif opcao==2:
        mult=n1*n2
        print("O resultado da multiplicacao entre {} e {} e igual a {}".format(n1,n2,mult))
    elif opcao==3:
        if n1>n2:
           maior=n1
        else:
            maior=n2
            print("Entre {} e {}, o numero maior e {}".format(n1,n2,maior))
    elif opcao==4:
        print("Digite novos numeros:")
        n1=int(input("Primeiro numero:"))
        n2=int(input("Segundo numero:"))
    elif opcao==5:
        print("Fim do programa")
    else:
        print("Opcao invalida")





