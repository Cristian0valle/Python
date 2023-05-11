import random

def hangman():
    palabras = ["python", "megadeth", "pantera", "random", "weed", "cristian", "ahorcado"]
    palabra_secreta = random.choice(palabras)
    intentos_restantes = 5
    letras_adivinadas = []
    juego_terminado = False

    print("Bienvenido al juego del Ahorcado!")
    print("La palabra secreta tiene: ", len(palabra_secreta), "letras.")
    print("========================================")

    while not juego_terminado:
        letra = input("Ingresa una letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_adivinadas:
                print("Ya has adivinado esa letra. Intenta con otra.")
                continue

            if letra in palabra_secreta:
                letras_adivinadas.append(letra)
                print("¡Correcto! La letra", letra, "está en la palabra secreta.")
            else:
                intentos_restantes -= 1
                print("Incorrecto. La letra", letra, "no está en la palabra secreta.")
                print("Te quedan", intentos_restantes, "intentos.")

            print("Letras adivinadas:", letras_adivinadas)

            # Verifica si se ha completado la palabra
            palabra_actual = ""
            for letra_secreta in palabra_secreta:
                if letra_secreta in letras_adivinadas:
                    palabra_actual += letra_secreta
                else:
                    palabra_actual += "_"
            print("Palabra actual:", palabra_actual)

            # Verifica si el jugador ganó o perdió
            if palabra_actual == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                juego_terminado = True
            elif intentos_restantes == 0:
                print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)
                juego_terminado = True
        else:
            print("Entrada inválida. Ingresa una sola letra.")

hangman()