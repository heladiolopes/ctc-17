import random as rd

"""
Legenda:
    '0': 
    'P': Pit
    'W': Wumpus
    'G': Gold
"""

cell_values = {
    '0': 0,  # Empty space
    'P': -50,  # Pit
    'W': -100,  # Wumpus
    'G': 100,  # Gold
}

movement_cost = -0.1

board = [
    ['0', 'P', '0', '0', '0', '0', 'P', '0'],
    ['W', 'G', 'P', '0', '0', '0', 'P', '0'],
    ['0', '0', '0', '0', 'W', 'G', '0', '0'],
    ['0', '0', 'P', '0', '0', '0', 'P', '0'],
]


class Tabuleiro:
    def __init__(self, init_tab):
        self.tab = init_tab
        self.size = (len(init_tab), len(init_tab[0]))
        self.__start_game()

    def randon_position(self):
        x = rd.randint(0, self.size[0] - 1)
        y = rd.randint(0, self.size[1] - 1)
        return x, y

    def __start_game(self):
        self.position = self.randon_position()

    def is_valid(self, position):
        if position[0] < 0 or position[0] >= self.size[0] or position[1] < 0 or position[1] >= self.size[1]:
            return False
        return True

    def sucessors(self, position):
        if self.tab[position[0]][position[1]] != '0':
            sc = []
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    sc.append((i, j))
            return sc

        cds = [
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1])
        ]
        sc = []
        parede = False
        for cd in cds:
            if self.is_valid(cd):
                sc.append(cd)
            elif not parede:
                sc.append((position[0], position[1]))
                parede = True
        return sc

    def next(self, position, action):
        if action == 'UP':
            return position[0] - 1, position[1]
        elif action == 'RIGHT':
            return position[0], position[1] + 1
        elif action == 'DOWN':
            return position[0] + 1, position[1]
        elif action == 'LEFT':
            return position[0], position[1] - 1
        else:
            return self.position

    def __mistake(self, position, action, mov='L'):
        k = 1 if (mov == 'L') else -1

        if action == 'UP':
            return position[0], position[1] - 1 * k
        elif action == 'RIGHT':
            return position[0] - 1 * k, position[1]
        elif action == 'DOWN':
            return position[0], position[1] + 1 * k
        elif action == 'LEFT':
            return position[0] + 1 * k, position[1]
        else:
            return position

    def transition_prob(self, position, action, next):

        if self.tab[position[0]][position[1]] != '0':
            return 1.0 / (self.size[0] * self.size[1])

        di = next[0] - position[0]
        dj = next[1] - position[1]

        not_valid_positions = (not self.is_valid(position)) or (not self.is_valid(next))
        nonadjacent_movement = abs(di) > 1 or abs(dj) > 1
        diagonal_movement = abs(di) != 0 and abs(dj) != 0

        if not_valid_positions or nonadjacent_movement or diagonal_movement:
            return 0.0

        if action == 'START':
            if di == 0 and dj == 0:
                return 1.0
            else:
                return 0.0

        quina = {
            (0, 0): {'U': 0.9, 'D': 0.0, 'L': 0.8, 'R': 0.0},
            (0, self.size[1]): {'U': 0.8, 'D': 0.0, 'L': 0.0, 'R': 0.9},
            (self.size[0], self.size[1]): {'U': 0.0, 'D': 0.9, 'L': 0.0, 'R': 0.8},
            (self.size[0], 0): {'U': 0.0, 'D': 0.8, 'L': 0.9, 'R': 0.0},
        }
        borda = [
            {'U': 0.7, 'D': 0.0, 'L': 0.1, 'R': 0.2},
            {'U': 0.1, 'D': 0.2, 'L': 0.0, 'R': 0.7},
            {'U': 0.0, 'D': 0.7, 'L': 0.2, 'R': 0.1},
            {'U': 0.2, 'D': 0.1, 'L': 0.7, 'R': 0.0},
        ]

        if di == 0 and dj == 0:
            h = (position[0] == 0) or (position[0] == self.size[0])
            v = (position[1] == 0) or (position[1] == self.size[1])
            if h and v:  # quina
                return quina[position][action[0]]

            elif h and not v:  # borda
                # 0 ou 2
                if position[0] == 0:
                    return borda[0][action[0]]
                else:
                    return borda[2][action[0]]

            elif not h and v:
                # 1 e 3
                if position[1] == 0:
                    return borda[3][action[0]]
                else:
                    return borda[1][action[0]]

        if next == self.next(position, action):
            return 0.7
        elif next == self.__mistake(position, action, 'L'):
            return 0.2
        elif next == self.__mistake(position, action, 'R'):
            return 0.1

        return 0.0

    def reward(self, position):
        x = 0

        # if not self.is_valid(self.next(position, action)):
        #     x = -1.0

        field = self.tab[position[0]][position[1]]
        return x + cell_values[field] + movement_cost

    def __str__(self):
        s = ''
        for i in range(4):
            for j in range(8):
                s += self.tab[i][j] + ' '
            s += '\n'

        return s


if __name__ == '__main__':
    tab = Tabuleiro(board)
    print(tab)
