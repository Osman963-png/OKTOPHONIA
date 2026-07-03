
from manim import *

class GoetheOctogono(ThreeDScene):

    def construct(self):

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=30 * DEGREES
        )

        self.begin_ambient_camera_rotation(rate=0.15)

        # Cores inspiradas em Goethe
        cores = [
            RED,
            ORANGE,
            YELLOW,
            GREEN,
            BLUE,
            PURPLE,
            MAROON,
            TEAL
        ]

        octogono = RegularPolygon(
            n=8,
            radius=3
        )

        self.play(Create(octogono))

        vertices = octogono.get_vertices()

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

        # Vértices coloridos
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
                font_size=24
            )

            texto.move_to(v * 1.3)

            pontos.add(ponto)
            textos.add(texto)

        self.play(FadeIn(pontos))
        self.play(Write(textos))

        # Camadas
        camadas = VGroup(
            Text("1 Cantus").scale(0.35),
            Text("2 Inversao").scale(0.35),
            Text("3 Retrogrado").scale(0.35),
            Text("4 Retro Inv").scale(0.35),
            Text("5 Expansao").scale(0.35),
            Text("6 Compressao").scale(0.35),
            Text("7 Pedal").scale(0.35),
            Text("8 Pulsos").scale(0.35),
        )

        camadas.arrange(DOWN)
        camadas.to_edge(RIGHT)

        self.play(FadeIn(camadas))

        # Cursor musical
        cursor = Dot(
            color=WHITE,
            radius=0.18
        )

        cursor.move_to(vertices[0])

        self.play(FadeIn(cursor))

        trajeto = [
            vertices[0],  # D
            vertices[1],  # Eb
            vertices[2],  # A
            vertices[3],  # B
            vertices[4],  # F#
            vertices[5],  # G
        ]

        for destino in trajeto[1:]:

            self.play(
                cursor.animate.move_to(destino),
                run_time=1
            )

        self.wait(5)
