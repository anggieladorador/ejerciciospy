#Escriba un programa que reciba como entrada las longitudes
#de los dos catetos a y b de un triángulo rectángulo,
#y que entregue como salida el largo de la hipotenusa
#c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

import math

print ("ingrese el primer cateto")
catetoA=int(input())
print("ingrese el segundo cateto")
catetoB=int(input())
hipotenusa= math.sqrt((catetoA**2)+(catetoB**2))
print(str(round(hipotenusa,2)))
