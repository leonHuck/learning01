totalMonto = 0 
datos = input("desea ingresar datos: ")
while datos == "si":
    monto = int(input("Ingrese un monto de sueldo que desea sumar: "))
    totalMonto = monto + totalMonto
    datos = input("desea iungresar otro dato? (si/no): ")
print("el total de dinero que tiene que tener para los sueldos es de: ", totalMonto)