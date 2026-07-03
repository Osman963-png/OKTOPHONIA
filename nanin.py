
from manim import *
import numpy as np

class OctogonoMusical3D(ThreeDScene):

    def construct(self):

        # -------------------
        # Câmera 3D
        # -------------------

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=45 * DEGREES
        )

        self.begin_ambient_camera_rotation(rate=0.15)

        # -------------------
        # Octógono
        # -------------------

        octogono = RegularPolygon(
            n=8,
            radius=3
        )

        octogono.set_color(WHITE)

        self.play(Create(octogono))

        vertices = octogono.get_vertices()

        # -------------------
        # Notas
        # -------------------

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

        labels = VGroup()

        for i, v in enumerate(vertices):

            texto = Text(
                notas[i],
                font_size=24
            )

            texto.move_to(v * 1.25)

            labels.add(texto)

        self.play(Write(labels))

        # -------------------
        # Camadas
        # -------------------

        camadas = VGroup(

            Text("1 Cantus").scale(0.4),
            Text("2 Inversão").scale(0.4),
            Text("3 Retrógrado").scale(0.4),
            Text("4 Retrógrado Inv.").scale(0.4),
            Text("5 Expansão").scale(0.4),
            Text("6 Compressão").scale(0.4),
            Text("7 Pedal").scale(0.4),
            Text("8 Pulsos").scale(0.4),

        )

        camadas.arrange(DOWN)

        camadas.to_edge(RIGHT)

        self.play(FadeIn(camadas))

        # -------------------
        # Trajeto Musical
        # -------------------

        trajeto = [
            vertices[0],  # D
            vertices[1],  # Eb
            vertices[2],  # A
            vertices[3],  # B
            vertices[4],  # F#
            vertices[5],  # G
        ]

        cursor = Sphere(
            radius=0.12,
            color=YELLOW
        )

        cursor.move_to(trajeto[0])

        self.play(FadeIn(cursor))

        for p in trajeto[1:]:

            self.play(
                cursor.animate.move_to(p),
                run_time=1
            )

        self.wait(2)

