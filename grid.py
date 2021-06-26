import random
import numpy as np

deltas = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def on_grid(x, y, m, n):
    return x >= 0 and y >= 0 and x < m and y < n

class GOL_Grid:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.dm = min(20, m//2)
        self.dn = min(20, n//2)
        self.grid1 = np.zeros(shape=(m + 2*self.dm, n + 2*self.dn))
        self.grid2 = np.zeros(shape=(m + 2*self.dm, n + 2*self.dn))

        self.curr = self.grid1
        self.neighbours = self.grid2
        self.grid_num = 1

    def print_grid(self):
        for i in range(self.dm, self.m + self.dm):
            for j in range(self.dn, self.n + self.dn):
                print(int(self.curr[i][j]), end=' ')
            print()

    def print_all(self):
        for i in range(self.m + 2*self.dm):
            for j in range(self.n + 2*self.dn):
                print(int(self.curr[i][j]), end=' ')
            print()

    def random_fill(self):
        for i in range(self.m + 2*self.dm):
            for j in range(self.n + 2*self.dn):
                self.curr[i][j] = random.randint(0,1)

    def count_neighbours(self, i, j):
        n_neighbours = 0
        for delta in deltas:
            if on_grid(i + delta[0], j + delta[1], self.m + 2*self.dm, self.n + 2*self.dn) \
            and self.curr[i + delta[0]][j + delta[1]] > 0:
                n_neighbours += 1
            if n_neighbours == 4:
                break
        return n_neighbours

    def do_next_gen(self):
        for i in range(self.m + 2*self.dm):
            for j in range(self.n + 2*self.dn):
                n_neighbours = self.count_neighbours(i, j)
                if self.curr[i][j] == 0:
                    if n_neighbours == 3:
                        self.neighbours[i][j] = 1
                    else: 
                        self.neighbours[i][j] = 0
                else: 
                    if n_neighbours in (2, 3):
                        self.neighbours[i][j] = 1
                    else: 
                        self.neighbours[i][j] = 0

        # Swap grids
        self.curr, self.neighbours = self.neighbours, self.curr

    def reset(self):
        self.curr.fill(0)

    def set_full(self, x, y):
        pass

    def set_gui(self, x, y):
        self.curr[x+self.dm][y+self.dn] = 1 if self.curr[x+self.dm][y+self.dn] == 0 else 0

