# Reducing_Combine_and_Conquer

This repository works on combining the divide and conquer tecnqiuce outlines by Nmaju et al, 2025 and
looking at the shape of the distribution we are encoding, Sarell et al. 2025 to further reduce the amount of gates n
needed to encode a distribution.

## Key files
All of the relevant programs can be found in the src folder.

circ_const.py, contains the main cruxs of the program and can be thought of as a mini libarys with key functions.

The other files are all for different example distributions.

BS- refers to the Black Schols distribution.

xxx_RCC_circ.py, means that file contains the reduced divide and conqure circuit required to encode that specific example.

xx_angle.py, contains the code needed to generate the relvant angles for that example.