football=(
    "Corinthians",
    "Palmeiras",
    "Santos",
    "Grêmio",
    "Cruzeiro",
    "Flamengo",
    "Vasco",
    "Chapecoense",
    "Atlético",
    "Botafogo",
    "Atlético-PR",
    "Bahia",
    "São Paulo",
    "Fluminense",
    "Sport",
    "Vitória",
    "Coritiba",
    "Avaí",
    "Ponte Preta",
    "Atlético-GO"
)
c=football.index("Chapecoense")
mais=c+1
print("As 5 primeiras equipas convocadas sao: {}".format(football[0:5]))
print("As 4 quatro equipas convocadas por ultimo sao: {} ".format(football[-4:]))
print(sorted(football))
print(" A equipa Chapecoense se encontra na {}º posicao na lista dos das equipas convocadas".format(mais))

