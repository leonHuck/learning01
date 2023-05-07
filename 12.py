""" Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.
 """
contadorMujeres = 0
nombresMujeres = " "
datos = input("Desea ingresar datos: (si/no)")
while datos == "si":
    nombre = str(input("ingrese su nombre: "))
    sexo = input("Ingrese su sexo: (hombre/mujer) ")
    if sexo == "mujer":
       contadorMujeres = contadorMujeres + 1
       nombresMujeres = nombre + nombresMujeres
    datos = input("Desea ingresar datos: (si/no)")
print("El total de mujeres es: ", contadorMujeres, "y sus nombres son: ", nombresMujeres)

