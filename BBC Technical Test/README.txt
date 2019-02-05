BBC SOFTWARE ENGINEERING TECHNICAL TEST

To run the game of life program type:

python gameoflife.py gameoflife_input

in the terminal/command line on a Linux/Mac machine.

The module dependencies are numpy and matplotlib and the program was written in Python 2.7.

I assumed that the boundary of the finite lattice of cells is periodic, so the cells on the border would interact
with the cells on the opposite side.

I applied a parallel update to the lattice at each iteration.  I stored a copy of the old lattice and applied the rules
to each cell in turn to determine each new cell state.  Then I updated all cell states of the real lattice
simultaneously.