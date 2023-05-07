totalPersonas = int(input("cuantas personas desea cargar: "))
totalEdades = 0 
for i in range(totalPersonas):
    edades = int(input("ingrese su edad: "))
    totalEdades = edades + totalEdades
promedio = totalEdades / totalPersonas
promedio = float(promedio)
print("El promedio de sus edades es ", round(promedio,1) )