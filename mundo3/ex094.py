teste=list()
teste.append("Jose")
teste.append(40)
print(teste)
galera=list()
galera.append(teste[:])
teste[0]="Joao"
teste[1]=22
galera.append(teste[:])
print(galera)
pessoas=[["Joao",19],["Paulo",40],["Jose",23],["Miguel",28],["Fernando",22]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')