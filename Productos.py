producto = float(input("Ingrese el precio del producto: " ))
sumatoria = 0 
cantidad_productos = 0


while (producto != 0) :
    cantidad_productos = cantidad_productos + 1
    sumatoria = sumatoria + producto
    producto = float(input("ingresa el precio de un producto:  0 para salir " ))
print("Hasta luego")
if (producto > 50000):
    descuento= producto * 0.70
    #precio_desc = producto - descuento
    print("El precio a pagar fue de: ",producto - descuento)
elif (producto < 50000):
    descuento= producto * 0.70
     #precio_desc = producto - descuento
    print("El precio a pagar fue de: ",producto - descuento)

