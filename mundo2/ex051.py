preco=float(input("Digite o valor do produto: "))
print("Opcoes de pagamento:")
print("1 - a vista dinheiro/cheque")
print("2 - a vista no cartao")
print("3 - 2x no cartao")
print("4 - 3x ou mais no cartao")
usuario=int(input("Como desejas fazer o pagamento?"))
if usuario== 1:
    total=preco-(preco*10/100)
elif usuario== 2:
    total=preco-(preco*5/100)
elif usuario== 3:
    total=preco
elif usuario== 4:
    parcelas=int(input("Quantas parcelas?"))
    total=preco+(preco*20/100)
    print("Sua compra sera parcelada em {} parcelas de R${}".format(parcelas,total/parcelas))
else:
    total=0
    print("Opcao invalida")

print("Total a pagar: R${}".format(total))


