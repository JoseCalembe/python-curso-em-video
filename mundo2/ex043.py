casa=float(input("Qual e o valor da casa?"))
salario=float(input("Qual e o valor do seu salario?"))
anos=int(input("Em quantos anos deseja pagar?"))
prestacao=(anos*12)
parcelas=casa/prestacao
limite=salario*30/100
print("Limite aceite {}".format(limite))
if parcelas<=limite:
   print("Seu emprestimo foi aprovado!")
   print("Voce pagara uma parcela de {:.2f} R$ a cada mes pelo emprestimo em {} prestacoes".format(parcelas,prestacao))
else:
    print("Seu emprestimo foi foi negado por eceder o limite!")
