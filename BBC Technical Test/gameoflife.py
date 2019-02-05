# BBC Software Engineering Technical Test
# Game of Life simulation
# By Simon McLaren

import numpy as np
import matplotlib.pyplot as plt
import sys

# Class to simulate the 'Game of Life'
class gameoflife():

    # 1: alive, 0: dead
    def __init__(self, init, lx, ly):

        # Define initial variables
        self.lx = int(lx) # number of cells in x direction
        self.ly = int(ly) # number of cells in y direction

        if init == 'Random': # Each cell is set as dead or alive by a 50/50 split
            self.lattice = np.random.choice([1, 0], size=(self.lx, self.ly))
        elif init == 'Allalive': # All cells alive
            self.lattice = np.ones((self.lx, self.ly), dtype=np.int)
        elif init == 'Alldead': # All cells dead
            self.lattice = np.zeros((self.lx, self.ly), dtype=np.int)

    # Reset lattice according to conditions defined by 'init'
    def reset_lattice(self, init):
        if init == 'Random':
            self.lattice = np.random.choice([1, 0], size=(self.lx, self.ly))
        elif init == 'Allalive':
            self.lattice = np.ones((self.lx, self.ly), dtype=np.int)
        elif init == 'Alldead':
            self.lattice = np.zeros((self.lx, self.ly), dtype=np.int)

    # Returns the number of nearest neighbour cells that are dead/alive, applying a periodic boundary
    def nearest_neighbours_dead_alive(self, cell):
        alive = 0
        dead = 0
        i = cell[0]
        j = cell[1]

        # Apply the periodic conditions at the boundary
        i_up = i + 1
        if i == self.lx - 1: i_up = 0
        j_up = j + 1
        if j == self.ly - 1: j_up = 0
        i_down = i - 1
        if i == 0: i_down = self.lx - 1
        j_down = j - 1
        if j == 0: j_down = self.ly - 1

        nearest_neighbours = [self.lattice[i][j_up], self.lattice[i][j_down],
                              self.lattice[i_up][j], self.lattice[i_down][j],
                              self.lattice[i_up][j_up], self.lattice[i_up, j_down],
                              self.lattice[i_down][j_down], self.lattice[i_down][j_up]]
        for nn in nearest_neighbours:
            if nn == 1:
                alive += 1
            elif nn == 0:
                dead += 1
        return dead, alive

    # Update the lattice in parallel and return it; according to the rules of the game of life
    def update(self):
        lattice_copy = np.copy(self.lattice)
        # Loop through all cells
        for i in range(self.lx):
            for j in range(self.ly):
                dead_nn, alive_nn = self.nearest_neighbours_dead_alive([i, j]) # Get dead/alive neighbours for current cell
                if self.lattice[i][j] == 1:
                    if alive_nn < 2 or alive_nn > 3:
                        lattice_copy[i][j] = 0
                elif self.lattice[i][j] == 0:
                    if alive_nn == 3:
                        lattice_copy[i][j] = 1
        return lattice_copy

    # Simulate a single lattice for N steps
    @staticmethod
    def simulate(lattice, N_steps, animate_freq, animate=False):
        for step in range(N_steps):
            print step
            if step % animate_freq == 0 and animate == True:
                plt.cla()
                im = plt.imshow(lattice.lattice, animated=True)
                plt.draw()
                plt.pause(0.0001)
            lattice.lattice = lattice.update()

def main():

    # Read input parameters from user via an input file
    if len(sys.argv) != 2:
        print "Wrong number of arguments."
        print "Usage: " + sys.argv[0] + " <input file>"
        quit()
    else:
        infileName = sys.argv[1]

    infile = open(infileName, 'r')

    # Extract input parameters
    line = infile.readline()
    tokens = line.split()

    init = str(tokens[0])
    size = int(tokens[1])
    sweeps = int(tokens[2])
    animate_freq = int(tokens[3])

    # Create game of life lattice
    lattice = gameoflife(init, size, size)

    # Animation
    fig = plt.figure()
    im = plt.imshow(lattice.lattice, vmin=0., vmax=1., cmap='jet', animated=True)
    plt.ion()

    # Simulate for the specified number of iterations
    gameoflife.simulate(lattice, sweeps, animate_freq, animate=True)

main()
