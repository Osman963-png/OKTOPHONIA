
import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

raio = 200

cores = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "magenta",
    "cyan"
]

camadas = [
    "Cantus",
    "Inversao",
    "Retrogrado",
    "Retro Invertido",
    "Expansao",
    "Compressao",
    "Pedal",
    "Pulsos"
]

# vértices do octógono
vertices = []

for i in range(8):
    a = math.radians(i * 45)
    x = raio * math.cos(a)
    y = raio * math.sin(a)
    vertices.append((x, y))


def desenhar_camada(i):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % 8]

    t.penup()
    t.goto(x1, y1)
    t.pendown()

    t.pencolor(cores[i])
    t.goto(x2, y2)

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    t.penup()
    t.goto(mx, my)
    t.write(camadas[i], align="center",
            font=("Arial", 10, "bold"))


# ------------------
# ANIMAÇÃO MUSICAL
# ------------------

# 0:00–0:30
desenhar_camada(0)  # C1
desenhar_camada(6)  # C7
time.sleep(5)

# 0:30–1:00
desenhar_camada(1)  # C2
desenhar_camada(4)  # C5
time.sleep(5)

# 1:00–1:30
desenhar_camada(2)  # C3
desenhar_camada(5)  # C6
desenhar_camada(7)  # C8
time.sleep(5)

# 1:30–2:00
desenhar_camada(3)  # C4

turtle.done()
