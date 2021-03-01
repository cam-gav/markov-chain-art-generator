# markov-chain-art-generator

Computational Creativity project that uses a Markov chain to generate turtle visual art.

Markov Chain art generator using turtle in Python.
The transition matrix probabilities were chosen by personal taste in deciding
how colors would best flow into each other.
Future iterations can include more interesting designs as well as a second
Markov Decision process that chooses the patterns that the turtle will follow.

## Dependencies:

numpy
## Instructions:

    1. Install dependencies
        python -m pip install --user numpy
    2. (Optional) Within the code, adjust the starting color from which future
        colors are chosen by changing the START_COLOR constant.
    3. (Optional) Within the code, adjust the length of the color palette by
        changing the NUM_COLORS int. If you choose a number (>6) or (<6 and not
        a factor of 6), then the colors of the rings will shift with each cycle.
    4. (Optional) Adjust the number of cycles to adjust the drawing duration.
    5. Run
