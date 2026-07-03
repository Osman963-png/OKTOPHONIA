
import turtle
import math

# -------------------------
# CONFIGURAÇÃO
# -------------------------

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")

t.speed(0)
t.pensize(3)
t.color("white")

raio = 180

# Camadas
camadas = [
    "C1 Cantus",
    "C2 Inversão",
    "C3 Retrógrado",
    "C4 Retro Inv",
    "C5 Expansão",
    "C6 Compressão",
    "C7 Pedal",
    "C8 Pulsos"
]

# Cores inspiradas em Goethe
cores = [
    "#cc0000",  # vermelho
    "#ff6600",  # laranja
    "#ffff00",  # amarelo
    "#00aa00",  # verde
    "#0088ff",  # azul
    "#6633cc",  # violeta
    "#990066",  # carmim
    "#333399"   # índigo
]

# -------------------------
# CÁLCULO DOS VÉRTICES
# -------------------------

vertices = []

for i in range(8):
    angulo = math.radians(45 * i)
    x = raio * math.cos(angulo)
    y = raio * math.sin(angulo)
    vertices.append((x, y))

# -------------------------
# DESENHO DO OCTÓGONO
# -------------------------

for i in range(8):

    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % 8]

    t.penup()
    t.goto(x1, y1)
    t.pendown()

    t.pencolor(cores[i])
    t.goto(x2, y2)

# -------------------------
# RÓTULOS DAS CAMADAS
# -------------------------

for i in range(8):

    x, y = vertices[i]

    t.penup()

    t.goto(x*1.15, y*1.15)

    t.pencolor(cores[i])

    t.write(
        camadas[i],
        align="center",
        font=("Arial", 10, "bold")
    )

# -------------------------
# NOTAS DA CÉLULA
# -------------------------

notas = [
    "D",
    "Eb",
    "F#",
    "G",
    "A",
    "B",
    "D*",
    "A*"
]

for i in range(8):

    x, y = vertices[i]

    t.penup()
    t.goto(x*0.85, y*0.85)

    t.pencolor("white")

    t.write(
        notas[i],
        align="center",
        font=("Arial", 14, "bold")
    )

# -------------------------
# CENTRO
# -------------------------

t.penup()
t.goto(0, 0)

t.pencolor("white")
t.write(
    "Célula\nD-Eb-A-B-F#-G",
    align="center",
    font=("Arial", 12, "bold")
)

# -------------------------
# EIXOS MUSICAIS
# -------------------------

for i in range(8):

    x, y = vertices[i]

    t.penup()
    t.goto(0, 0)

    t.pendown()
    t.pencolor(cores[i])

    t.goto(x, y)

t.hideturtle()
turtle.done()