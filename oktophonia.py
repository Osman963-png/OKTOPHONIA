
from manim import *

class Oktophonia(ThreeDScene):

    def construct(self):

        # -----------------------------
        # CÂMERA
        # -----------------------------

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=35 * DEGREES
        )

        self.begin_ambient_camera_rotation(
            rate=0.10
        )

        # -----------------------------
        # OCTÓGONO
        # -----------------------------

        octogono = RegularPolygon(
            n=8,
            radius=3,
            color=WHITE
        )

        self.play(Create(octogono))

        vertices = octogono.get_vertices()

        # -----------------------------
        # CORES DE GOETHE
        # -----------------------------

        cores = [
            RED,       # D
            ORANGE,    # Eb
            YELLOW,    # A
            GREEN,     # B
            BLUE,      # F#
            PURPLE,    # G
            MAROON,    # D+A
            TEAL       # Pulso
        ]

        # -----------------------------
        # NOTAS
        # -----------------------------

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

        pontos = VGroup()
        textos = VGroup()

        for i, v in enumerate(vertices):

            ponto = Dot(
                point=v,
                color=cores[i],
                radius=0.12
            )

            texto = Text(
                notas[i],
                font_size=28
            )

            texto.move_to(v * 1.25)

            pontos.add(ponto)
            textos.add(texto)

        self.play(FadeIn(pontos))
        self.play(Write(textos))

        # -----------------------------
        # CAMADAS
        # -----------------------------

        camadas = VGroup(

            Text("1 Cantus").scale(0.4),
            Text("2 Inversao").scale(0.4),
            Text("3 Retrogrado").scale(0.4),
            Text("4 Retrogrado Invertido").scale(0.4),
            Text("5 Expansao").scale(0.4),
            Text("6 Compressao").scale(0.4),
            Text("7 Pedal").scale(0.4),
            Text("8 Pulsos").scale(0.4)

        )

        camadas.arrange(DOWN)
        camadas.to_edge(RIGHT)

        # -----------------------------
        # TEMPORALIDADE
        # -----------------------------

        self.play(
            FadeIn(camadas[0]),
            FadeIn(camadas[6])
        )

        self.wait(1)

        self.play(
            FadeIn(camadas[1]),
            FadeIn(camadas[4])
        )

        self.wait(1)

        self.play(
            FadeIn(camadas[2]),
            FadeIn(camadas[5]),
            FadeIn(camadas[7])
        )

        self.wait(1)

        self.play(
            FadeIn(camadas[3])
        )

        # -----------------------------
        # TRAJETO MUSICAL
        # -----------------------------

        trajeto = [
            vertices[0],   # D
            vertices[1],   # Eb
            vertices[2],   # A
            vertices[3],   # B
            vertices[4],   # F#
            vertices[5]    # G
        ]

        cursor = Dot(
            color=WHITE,
            radius=0.20
        )

        cursor.move_to(trajeto[0])

        self.play(FadeIn(cursor))

        # -----------------------------
        # DESENHO DA LINHA MUSICAL
        # -----------------------------

        for i in range(len(trajeto)-1):

            linha = Line(
                trajeto[i],
                trajeto[i+1],
                color=YELLOW
            )

            self.play(
                Create(linha),
                cursor.animate.move_to(
                    trajeto[i+1]
                ),
                run_time=1.2
            )

        # -----------------------------
        # PEDAL D-A
        # -----------------------------

        pedal1 = Circle(
            radius=0.35,
            color=RED
        )

        pedal1.move_to(vertices[0])

        pedal2 = Circle(
            radius=0.35,
            color=BLUE
        )

        pedal2.move_to(vertices[2])

        self.play(
            FadeIn(pedal1),
            FadeIn(pedal2)
        )

        # -----------------------------
        # PULSOS
        # -----------------------------

        for _ in range(3):

            pulso = Circle(
                radius=0.2,
                color=WHITE
            )

            pulso.move_to(vertices[7])

            self.play(
                GrowFromCenter(pulso),
                run_time=0.5
            )

            self.remove(pulso)

        # -----------------------------
        # TÍTULO
        # -----------------------------

        titulo = Text(
            "OKTOPHONIA",
            font_size=32
        )

        titulo.to_edge(UP)

        self.play(Write(titulo))

        self.wait(5)
