import random
from math import exp, pi, cos, sin
from datetime import datetime as dt


class Board:
    def __init__(self, board):
        self.board = board

        self.n = len(board)
        self.total = self.n*(self.n - 1)/2

    def cost_function(self):
        wrong = 0
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                if self.board[i] == self.board[j] or (abs(self.board[i] - self.board[j]) == abs(i - j)):
                    wrong += 1
        return wrong

    def neighbors(self):
        all_neighbors = []
        for i in range(self.n):
            for j in range(self.n):
                if j != self.board[i]:
                    aux = self.n * [0]
                    for k in range(self.n):
                        aux[k] = self.board[k]
                    aux[i] = j
                    all_neighbors.append(Board(aux))
        return all_neighbors

    def random_neighbor(self):
        all_neighbors = self.neighbors()
        return random.choice(all_neighbors)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost_function(self):
        x = self.x
        y = self.y
        val = 4*exp(-(x**2 + y**2)) + exp(-((x-5)**2 + (y-5)**2)) + exp(-((x+5)**2 + (y-5)**2)) + exp(-((x-5)**2 + (y+5)**2)) + exp(-((x+5)**2 + (y+5)**2))
        return val

    def neighbors(self):
        x = self.x
        y = self.y
        delta = 0.01
        num_neighbors = 8

        all_neighbors = []
        for i in range(num_neighbors):
            point = Point(delta*cos(2*pi*i/num_neighbors) + x, delta*sin(2*pi*i/num_neighbors) + y)
            all_neighbors.append(point)
        return all_neighbors


def hill_climbing(initial):
    max_iterations = 1000

    theta = initial
    best = initial

    i = 0
    while i < max_iterations:
        list_neighbors = theta.neighbors()
        for neighbor in list_neighbors:
            if neighbor.cost_function() > best.cost_function():
                best = neighbor
        if best.cost_function() < theta.cost_function():
            return theta.x, theta.y, theta.cost_function()
        theta = best
        i += 1
    return theta.x, theta.y, theta.cost_function()


def simulated_annealing(initial):
    theta = initial

    t0 = 1.0
    beta = 1.0
    i = 0
    while theta.cost_function() > 0:
        t = float(t0/(1 + beta*i*i))
        if t <= 0.0:
            return theta.cost_function()
        neighbor = theta.random_neighbor()
        delta = float((neighbor.cost_function() - theta.cost_function()))
        if delta <= 0.0 or exp(-delta/t) >= random.random():
            theta = neighbor
        i += 1
    return theta.cost_function()


if __name__ == "__main__":
    initial_board_1 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    initial_board_2 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    initial_board_3 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    initial_board_4 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    # N-Queens
    """
    t = [0.0, 0.0, 0.0, 0.0]
    N = 100
    for i in range(N):
        myTime = dt.now()
        cost_1 = simulated_annealing(initial_board_1)
        t[0] += (dt.now() - myTime).total_seconds()

        myTime = dt.now()
        cost_2 = simulated_annealing(initial_board_2)
        t[1] += (dt.now() - myTime).total_seconds()

        myTime = dt.now()
        cost_3 = simulated_annealing(initial_board_3)
        t[2] += (dt.now() - myTime).total_seconds()

        myTime = dt.now()
        cost_4 = simulated_annealing(initial_board_4)
        t[3] += (dt.now() - myTime).total_seconds()

    for i in range(4):
        t[i] = t[i]/(float(N))
    """

    # Glocal and Local Maximums
    """
    initial_point = Point(2.0, 2.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(-2.0, -2.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(2.0, -2.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(-2.0, 2.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(4.0, 4.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(-4.0, -4.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(4.0, -4.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)

    initial_point = Point(-4.0, 4.0)
    x, y, cost = hill_climbing(initial_point)
    print(x, y, cost)
    """

