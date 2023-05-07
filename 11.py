""" Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un cartel por cada uno.
 """
repeticiones = 7
for x in range(repeticiones):
    numero = int(input("ingrese un numero entero: "))
    if numero >= 1 and numero <= 9:
        print("Su numero es un numero natural de una sola cifra!!!")
