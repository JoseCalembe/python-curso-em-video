n=input(r'Qual e o metodo de cobranca? (dias/km)').upper().lower()
while n!="dias" and n!="km":
      print("Metodo invalido, escolha apenas entre: (dias/km)")
      n=input(r'Qual e o metodo de cobranca? (dias/km)')
if n=="dias":
    d=int(input("Por quantos dias o carro foi alugado?"))
    pagamento_por_dias=d*80
    print("Voce escolheu pagar o aluguel do carro consoante o numero de dias")
    print("Nesse caso como o carro foi alugado por {} dias voce pagara um total de {:.2f} R$ pelo aluguel".format(d,pagamento_por_dias))

elif n=="km":
    k=float(input("Quantos Km o carro percorreu durante o periodo em que o carro foi alugado?"))
    pagamento_por_km = (k*1.70)
    print("Voce esolheu em pagar o aluguel do carro consoante o numero de Km percorrido")
    print("Nesse caso como o carro percorreu {} Km durante o periodo em que voce alugou, o pagamento sera de {:.2f} R$ pelo aluguel".format(k,pagamento_por_km))

print("Muito obrigdo por teres escolhido o nosso servico!")
print("Volte sempre!")

