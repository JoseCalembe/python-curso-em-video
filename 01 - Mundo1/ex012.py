while True:
    altura=float(input("digite a altura da parede :"))
    largura=float(input("digite a largura da parede :"))
    unidade=str(input("digite a unidade da altura e da largura :"))

    while unidade not in "Mm":
      unidade = str(input("digite a unidade da altura e da largura :"))
    if unidade in "Mm":
       area=altura*largura
       tinta=area/2
       break
print("A sua parede tem uma area de {}m²".format(area))
print("Nesse caso precisaremos no total {:.2f} l de tinta para pintar a parede toda".format(tinta))