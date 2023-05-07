""" Dada una lista de nombres y de salarios respectivos, 
determinar el salario mínimo y mostrar el nombre de la persona que menos gana.
 """
menorSalario = 1_000_000_000
cantidadempleados = int(input("De cuantos empleados es la lista que va a cargar: "))
for x in range(cantidadempleados):
    empleado = input("ingrese su nombre: ")
    salario = int(input("Cuanto gana: "))
    if salario < menorSalario:
        menorSalario = salario
        empleadoPobre = empleado
print(empleadoPobre,"gana", menorSalario)

