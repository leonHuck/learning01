""" Ingresar la lluvia caída en milímetros para cada día de la semana.
 Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.
 """
sinLluvia = 0 
totalLluvia = 0
for x in range(7):
    dia = input("ingrese que dia es: ")
    lluvia = int(input("Cuanto llovio hoy, en milimetros: "))
    if lluvia == 0:
        sinLluvia = sinLluvia + 1
    else:
        totalLluvia = totalLluvia + lluvia
print("Tottal de lluvia: ", totalLluvia, "Y la cantidad de dias que no llovieron son: ", sinLluvia )

