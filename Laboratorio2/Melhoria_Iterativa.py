# Problema das N-Rainhas
# Hill Climbing ou Simulated Annealing
# N = 10, 15, 20, 25
# Tabelar tempo de processamento

# Determinar o máximo global da função
# Hill Climbing ou Simulated Annealing
# f(x, y) = 4*e^(-(x^2 + y^2)) + e^(-((x - 5)^2 + (y - 5)^2)) + e^(-((x + 5)^2 + (y - 5)^2)) +
# e^(-((x - 5)^2 + (y + 5)^2)) + e^(-((x + 5)^2 + (y + 5)^2))
# Máximo local

import random
from math import exp


class Board:
    def __init__(self, board):
        self.board = board

        self.n = len(board)
        self.total = self.n*(self.n - 1)/2

    def cost_function(self):
        wrong = 0
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                if self.board[i] == self.board[j] or (abs(i - self.board[i]) == abs(j - self.board[j])):
                    wrong += 1
        return wrong

    def neighbors(self):
        all_neighbors = []
        for i in range(self.n):
            if self.board[i] > 0:
                aux = self.n*[0]
                for j in range(self.n):
                    if i == j:
                        aux[j] = self.board[j] - 1
                    else:
                        aux[j] = self.board[j]
                all_neighbors.append(Board(aux))

            if self.board[i] < self.n - 1:
                aux = self.n * [0]
                for j in range(self.n):
                    if i == j:
                        aux[j] = self.board[j] + 1
                    else:
                        aux[j] = self.board[j]
                all_neighbors.append(Board(aux))
        return all_neighbors

    def random_neighbor(self):
        all_neighbors = self.neighbors()
        return random.choice(all_neighbors)

class Methods:
    def __init__(self):
        pass

    def hill_climbing(self, initial):
        theta = initial
        history = [initial]

        best = initial

        while theta.cost_function() > 0:
            list_neighbors = theta.neighbors()
            for neighbor in list_neighbors:
                if neighbor.cost_function() < best.cost_function():
                    best = neighbor
            if best.cost_function() > theta.cost_function():
                return theta.cost_function, history
            theta = best
            history.append(theta)
        return theta.cost_function, history

    def simulated_annealing(self, initial):
        theta = initial
        history = [initial]

        t0 = 1.0
        beta = 1.0
        i = 0
        while theta.cost_function() > 0:
            print(theta.board, theta.cost_function())
            t = t0/(1 + beta*i*i)
            if t <= 0.0:
                return theta.cost_function(), history
            neighbor = theta.random_neighbor()
            delta = (theta.cost_function() - neighbor.cost_function())
            if delta > 0:
                theta = neighbor
            else:
                r = random.uniform(0.0, 1.0)
                if r <= exp(delta/t):
                    theta = neighbor
            history.append(theta)
            i += 1
        return theta.cost_function(), history


if __name__ == "__main__":
    initial_board_1 = Board([0, 1, 2, 3])
    #initial_board_1 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    initial_board_2 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    initial_board_3 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    initial_board_4 = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    all_Methods = Methods()
    cost, history = all_Methods.simulated_annealing(initial_board_1)
    print(cost)

