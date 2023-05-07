contador = 0 
print("A continuacion tendras que ingresar 5 numeros, los mayores a 23 los contare")
for i in range(5):
    number = int(input("ingrese un numero "))
    if number > 23:
        contador = number + contador
print("la suma de sus numeros mayores a 23 es: ", contador)


        

