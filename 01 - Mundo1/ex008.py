medida=float(input("uma distancia em metros:"))
km=medida/1000
hm=medida/100
dam=medida/10
dm=medida/10
cm=medida*100
mm=medida*1000
print("a medida em{}m corresponde a {:.0f}km" .format(medida,km))
print("a medida em{}m corresponde a {:.0f}hm" .format(medida,hm))
print("a medida em{}m corresponde a {:.0f}dam" .format(medida,dam))
print("a medida em{}m corresponde a {:.0f}dm" .format(medida,dm))
print("a medida em{}m corresponde a {:.0f}cm" .format(medida,cm))
print("a medida em{}m corresponde a {:.0f}mm" .format(medida,mm))
#print("A medida em {}m corresponde a {:.0f}cm e {:.0f}mm".format(medida,medida*100,medida*1000))
