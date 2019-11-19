#Escriba un programa que pregunte al usuario la hora actual t del reloj
#y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

print("por favor ingrese la hora actual")
t = int(input())

print("ingresa la cantidad de horas")
h = int(input())

nuevaHora = t+h

if(nuevaHora > 12):
    diferencia = h%12
    newH = diferencia + t #7 horas
    if(newH==13):
       print("marcará las 1")
    elif(newH==14):
        print("marcará las 2")
    elif(newH==15):
        print("marcará las 3")
    elif(newH==16):
        print("marcará las 4")
    elif(newH==17):
        print("marcará las 5")
    elif(newH==18):
        print("marcará las 6")
    elif(newH==19):
        print("marcará las 7")
    elif(newH==20):
        print("marcará las 8")
    elif(newH==21):
        print("marcará las 9")
    elif(newH==22):
        print("marcará las 10")
    elif(newH==23):
        print("marcará las 11")
    else:
        print("marcará las 12")   
else:
    print("el reloj marcará :"+str(nuevaHora))






