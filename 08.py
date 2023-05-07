valorAuto = ""
valorTotal = 0 
while valorAuto != 0:
    autos = str(input("Que auto desea cargar: "))
    valorAuto = int(input("Ingrese el valor del auto que desea cargar: "))
    if valorAuto >= 3_460_000 and 12_850_000 >= valorAuto :
        valorTotal = valorTotal + 1 
        
print("La cantidad de autos que valen entre 3.460.000 y 12.850.000 son: ", valorTotal)
