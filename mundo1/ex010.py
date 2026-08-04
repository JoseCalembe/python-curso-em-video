tem=float(input("digite uma temperatura em graus Celsius:"))
kelvin=(tem+273.15)
fahrenheit=(9/5*tem+32)
Rankine=(tem+273.15*9/5)
reaumur=(4/5*tem)
print(" convertendo {}graus celcious para kelvin e:{:.2f}kelvin".format(tem,(tem+273.15)))
print(" convertendo {}graus celcious para fahrenheit e:{:.0f}fahrenheit".format(tem,(9/5*tem+32)))
print(" convertendo {}graus celcious para Rankine  e:{:.2f}Rankine".format(tem,(tem+273.15)*9/5))
print(" convertendo {}graus celcious para reaumur  e:{:.0f}reaumur".format(tem,(4/5*tem)))






