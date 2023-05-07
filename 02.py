hayDatos = input("tiene datos que ingresar: (si/no): ")
while hayDatos == "si":
    numero = int(input("Ingrese un numero: "))
    if numero <= 0:
        print("su numero es negativo")
    else:
        print("su numero es positivo")
    hayDatos = input("tiene mas datos que ingresar: (si/no): ")
    

