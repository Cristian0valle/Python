
print("Calculadora")

try: 
    valor1 = int(input("ingresa el primer valor: "))
    valor2 = int(input("ingresa el segundo valor: "))   
    Suma = valor1+valor2
    resta = valor1-valor2
    Multiplicacion = valor1*valor2
    division = valor1/valor2

except ValueError as err: #capturamos ValueError que muestra el error de caracter incorrecto
    print("Error: Caracter invalido",err)
    valor1=0   #dejamos un valor por defecto
    valor2=0

except ZeroDivisionError as err:  #capturamos ZeroDivisionError que muestra que no se puede dividir por cero
    print("Error: no se puede dividir por Cer0") 

finally:        #Siempre se ejecuta 
    print("Suma: ",Suma)
    print("Resta",resta)
    print("multiplicacion",Multiplicacion)
    print("division",division)



