'''Los parametros que tengan valores por default, siempre se deben leer de derecha a izquierda
siempre deben estar a la derecha
'''
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)



print(area_circulo(10))