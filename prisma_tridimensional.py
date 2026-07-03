
import turtle
import math

# -----------------------------------
# CONFIGURAÇÃO
# -----------------------------------

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1000, 800)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Cores inspiradas em Goethe
cores = [
    "#cc0000",  # vermelho
    "#ff6600",  # laranja
    "#ffff00",  # amarelo
    "#00cc00",  # verde
    "#0088ff",  # azul
    "#6633cc",  # violeta
    "#990066",  # carmim
    "#333399"   # índigo
]

camadas = [
    "C1",
    "C2",
    "C3",
    "C4",
    "C5",
    "C6",
    "C7",
    "C8"
]

# -----------------------------------
# FUNÇÃO OCTÓGONO
# -----------------------------------

def octogono(cx, cy, raio):
    pontos = []

    for i in range(8):
        ang = math.radians(45 * i + 22.5)

        x = cx + raio * math.cos(ang)
        y = cy + raio * math.sin(ang)

        pontos.append((x, y))

    return pontos


# base inferior
base = octogono(0, -100, 180)

# base superior deslocada
topo = octogono(80, 80, 180)

# -----------------------------------
# DESENHAR FACES
# -----------------------------------

for i in range(8):

    x1, y1 = base[i]
    x2, y2 = base[(i + 1) % 8]

    t.pencolor(cores[i])

    t.penup()
    t.goto(x1, y1)
    t.pendown()

    t.goto(x2, y2)


for i in range(8):

    x1, y1 = topo[i]
    x2, y2 = topo[(i + 1) % 8]

    t.pencolor(cores[i])

    t.penup()
    t.goto(x1, y1)
    t.pendown()

    t.goto(x2, y2)


# -----------------------------------
# LIGAÇÕES VERTICAIS
# -----------------------------------

for i in range(8):

    xb, yb = base[i]
    xt, yt = topo[i]

    t.pencolor(cores[i])

    t.penup()
    t.goto(xb, yb)
    t.pendown()

    t.goto(xt, yt)


# -----------------------------------
# RÓTULOS DAS CAMADAS
# -----------------------------------

for i in range(8):

    xb, yb = base[i]
    xt, yt = topo[i]

    mx = (xb + xt) / 2
    my = (yb + yt) / 2

    t.penup()
    t.goto(mx, my)

    t.pencolor("white")

    t.write(
        camadas[i],
        align="center",
        font=("Arial", 10, "bold")
    )

# -----------------------------------
# NOTAS MUSICAIS
# -----------------------------------

notas = [
    "D",
    "Eb",
    "A",
    "B",
    "F#",
    "G",
    "D+A",
    "Pulso"
]

for i in range(8):

    xt, yt = topo[i]

    t.penup()
    t.goto(xt * 1.05, yt * 1.05)

    t.pencolor("white")

    t.write(
        notas[i],
        align="center",
        font=("Arial", 12, "bold")
    )

# -----------------------------------
# CENTRO
# -----------------------------------

t.penup()
t.goto(40, 0)

t.pencolor("white")

t.write(
    "PRISMA OCTOGONAL\nMUSICAL",
    align="center",
    font=("Arial", 14, "bold")
)

t.hideturtle()

turtle.done()


