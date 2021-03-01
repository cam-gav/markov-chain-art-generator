# markov-chain-art-generator

Computational Creativity project that uses a Markov chain to generate turtle
visual art.

This Markov Chain utilizes the turtle import in Python. I wanted to revisit the
turtle lessons from 1101 and apply Computational Creativity concepts to them.
This nostalgic return to turtle was also personal to me because I am currently
very interesting in the cyberpunk aesthetic. I love neon colors and sharp edges
on a dark background. Some of the art produced by this program is reminiscent of
the Tron: Legacy movie. This Markov Chain makes me think of how robots might
handle artistic creation in a cyberpunk future.

The transition matrix probabilities were chosen by personal taste in deciding
how colors would best flow into each other. Choosing probabilities was a
surprisingly creative and complex endeavor. It required predicting what
possibilities could come from each number in the matrix. Did I want all the
colors to flow into each other or only some colors to be intimitely related and
produced together in the final piece?
I had to balance my artistic input versus giving the Markov Chain more
randomness/autonomy.
Future iterations can include more interesting designs as well as a second
Markov Decision process that chooses the patterns that the turtle will follow.
Other possiblities include exploring more color transitions and having a markov
chain which takes into account multiple previous colors added to the color
palette.

For this this divergent thinking assignment, I believe my system is P-creative
because it is novel to me. Never before have I created turtle art according to a
Markov Chain transition matrix.
This project can also become quite H-creative in the sense that it could grow
and become so niche that no one has seen or thought of it before. For example,
the program could be extended and complicated in order to produce novel neon
sign graphic designs for a video game. Elaboration and originality can really
become the fortes of this sort of project.

## Dependencies

numpy

## Instructions

    1. Install dependencies
        python -m pip install --user numpy
    2. (Optional) Within the code, adjust the starting color from which future
        colors are chosen by changing the START_COLOR constant.
    3. (Optional) Within the code, adjust the length of the color palette by
        changing the NUM_COLORS int. If you choose a number (>6) or (<6 and not
        a factor of 6), then the colors of the rings will shift with each cycle.
    4. (Optional) Adjust the number of cycles to adjust the drawing duration.
    5. Run

## Sources

* Dr. Sarah Harmon's markov_musician program
