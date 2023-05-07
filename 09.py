""" Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. 
Se deberá ir preguntando si hay más números para ingresar.
 """

cantidadNumero = int(input("Cuantos numeros reales desea ingresar: "))
numeroMaximo = 0
for i in range(cantidadNumero):
    numero = int(input("Ingrese un numero real positivo: "))
    if numero > numeroMaximo:
        numeroMaximo = numero 
masNumeros = input("desea ingresar mas numeros: (si/no)")
while masNumeros == 'si':
    numero = int(input("Ingrese un numero real positivo: "))
    if numero > numeroMaximo:
        numeroMaximo = numero 
    masNumeros = input("desea ingresar mas numeros: (si/no)")
print("El numero maximo que ingreso es: ",numeroMaximo)

