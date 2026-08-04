altura=float(input("Qual e a altura da parede em metros: "))
largura=float(input("Qual e a largura da parede em metros: "))
Area=altura*largura
Tinta=Area/2
print("A sua parede tem uma dimensao de {}m x {}m e uma Area de {}m² ".format(altura,largura,Area))
print("Para pintar a parede precisaras de {}L de tinta ".format(Tinta))