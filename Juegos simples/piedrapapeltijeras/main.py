import random


def cachipun():
    print("""Bienvenido a jugar cachipun!! Las instrucciones son las siguientes:
    Selecciona: "A" para usar PAPEL
    Selecciona: "S" para usar PIEDRA
    Selecciona: "D" para usar TIJERAS
    Selecciona: "Q" para salir""")

    opciones = {'A': 'PAPEL', 'S': 'PIEDRA', 'D': 'TIJERAS'}

    while True:
        usuario = input("Selecciona una letra: ").upper()
        computadora = random.choice(list(opciones.keys()))

        if usuario == 'Q':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        elif usuario in opciones:
            print(f"Computadora eligió: {opciones[computadora]}")
            print(f"Tú elegiste: {opciones[usuario]}")

            if usuario == computadora:
                print("¡Es un empate!")
            elif (usuario == 'S' and computadora == 'D') or (usuario == 'A' and computadora == 'S') or (usuario == 'D' and computadora == 'A'):
                print("Ganaste!!! ")
            else:
                print("Perdiste! :c")
        else:
            print("Selecciona una opcion correcta men... A - S - D")


cachipun()
