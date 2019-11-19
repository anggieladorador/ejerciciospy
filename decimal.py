#Parte decimal 
# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
print("ingrese un numero decimal")
numero = float(input())
numeroredondeado = round(numero)
partedecimal  =numeroredondeado- numero 
print(round(partedecimal, 3))