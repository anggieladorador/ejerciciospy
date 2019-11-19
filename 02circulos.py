#CIRCULOS
#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5
import math

print("ingrese radio")
radious = int(input())

perimeter = 2*(math.pi)*radious
area = (math.pi)*radious**2
print(perimeter, area)  