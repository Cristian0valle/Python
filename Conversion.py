from fastapi import FastAPI

# Configurar la ventana de dibujo
wn = turtle.Screen()
wn.bgcolor("black") # Fondo negro
wn.title("Animación de Círculo Centrado")
wn.setup(width=1.0, height=1.0) # Maximizar ventana de dibujo

# Configurar la tortuga
t = turtle.Turtle()
t.speed(0) # Velocidad máxima de la tortuga
t.color("cyan") # Color de la tortuga

# Calcular el radio del círculo
radius = min(wn.window_width() // 2, wn.window_height() // 2) - 50

# Posicionar la tortuga en el centro del círculo
t.penup()
t.goto(0, -radius)
t.pendown()

# Animación del círculo centrado
for i in range(360): # Repetir 360 veces para un círculo completo
    t.forward(radius * 2 * 3.1415 / 360) # Avanzar una fracción del perímetro del círculo
    t.left(1) # Girar a la izquierda

# Cerrar la ventana al hacer clic
wn.exitonclick()

# Cerrar la ventana al hacer clic
wn.exitonclick()