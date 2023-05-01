sumatoria = 0 
cantidad_productos = 0
nota= float(input("Ingrese una nota (0 para salir)"))
while(nota != 0 ):
    sumatoria = sumatoria + nota
    cantidad_productos = cantidad_productos + 1
    nota = float(input("Ingrese una nota (0 para salir)"))
if (cantidad_productos > 0):
    promedio = sumatoria/ cantidad_productos
    print("el prpomedio es: ", promedio)

