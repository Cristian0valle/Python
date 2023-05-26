tupla1 = ("primer elemento", "segundo elemento", "tercer elemento", "cuarto elemento")

#la principal diferencia de una tupla con una lista es; que la tupla es inmutable

print(tupla1[0:2])  #esto recorre la tupla desde el elemento 0 al 1, llega al 2 y se detiene

#mezclar tuplas
tupla2 = ("quinto elemento", "sexto elemento")
tupla3 = tupla1 + tupla2

for x in tupla3:
    print(x)
