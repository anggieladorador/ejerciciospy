#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
notas = []
suma =0
for i in range (4): 
    print("ingrese su nota")
    i = int(input())
    notas.append(i)

for i, nota in enumerate(notas):
    numero = i+1
    print("nota "+str(numero)+": "+ str(nota))
    suma = suma + nota
prom = suma/len(notas)
print(str(prom))
