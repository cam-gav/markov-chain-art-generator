"""
Markov Chain art generator using turtle in Python.

Dependencies: numpy

Author: Camilo Pareja
Date: February 2021
"""

import turtle
import numpy as np

turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(2)

START_COLOR = "yellow"
NUM_COLORS = 6
CYCLES = 4 
# Number of cycles to repeat the generated art pattern. More cycles means more 
# time viewing the art being generated.

class MarkovArtist:
    def __init__(self, transition_matrix):
        """Simulates a turtle artist that utilizes a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.colors = list(transition_matrix.keys())
    
    def get_next_color(self, current_color):
        """Decides which color to pick next based on the current color.
           Args:
               current_note (str): the current note being played.
        """
        return np.random.choice(
            self.colors,
            p=[self.transition_matrix[current_color][next_color] \
            for next_color in self.colors]
        )

    def compose_palette(self, current_color="red", palette_length=6):
        """Generates a sequence of colors.
           Args:
                current_color (str): the color of the palette that we are 
                currently looking at.

                palette_length (int): how many colors we should generate for the
                final art piece.
        """
        palette = []

        while len(palette) < palette_length:
            next_color = self.get_next_color(current_color)
            palette.append(next_color)
            current_color = next_color

        return palette


def main():
    art_maker = MarkovArtist({
        "red": {"red": 0.2, "magenta": 0.6, "blue": 0.0, "cyan": 0.0, "green": 0.0, "yellow": 0.2},
        "magenta": {"red": 0.3, "magenta": 0.3, "blue": 0.2, "cyan": 0.1, "green": 0.1, "yellow": 0.0},
        "blue": {"red": 0.0, "magenta": 0.3, "blue": 0.1, "cyan": 0.2, "green": 0.2, "yellow": 0.2},
        "cyan": {"red": 0.0, "magenta": 0.2, "blue": 0.5, "cyan": 0.2, "green": 0.0, "yellow": 0.1},
        "green": {"red": 0.0, "magenta": 0.0, "blue": 0.0, "cyan": 0.3, "green": 0.1, "yellow": 0.6},
        "yellow": {"red": 0.2, "magenta": 0.2, "blue": 0.2, "cyan": 0.2, "green": 0.1, "yellow": 0.1}
    })

    new_palette = art_maker.compose_palette(START_COLOR, NUM_COLORS)
    print("Here's my latest turtle art palette: ", new_palette)

    print("Letting the turtle artist do its thing!")
    for cycle in range(CYCLES):
        for i in range(6):
            for color in new_palette:
                turtle.color(color)
                turtle.forward(150)
                turtle.right(62)
                turtle.forward(150)
                turtle.right(62)
                turtle.forward(150)
                turtle.right(62)
                turtle.forward(150)
                turtle.right(62)
                turtle.forward(150)
                turtle.right(62)
                turtle.forward(150)
                turtle.right(62)
                turtle.right(10)
                
    print("Process completed! The turtle will now go back to its humble abode.")
    turtle.hideturtle()


if __name__ == "__main__":
    main()
