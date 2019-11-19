print("ingrese un numero de tres digitos")
value = input()
print(value[len(value)::-1])

#metodo slicing
#se crea un slice que empieza desde el largo de la cadena
#termina en el index cero y que va hacia atras
print("**********")

alreves = "".join(reversed(value))
print(alreves)
