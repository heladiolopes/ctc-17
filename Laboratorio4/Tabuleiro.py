import random as rd
"""
Legenda:
    '0': 
    'P': Pit
    'W': Wumpus
    'G': Gold
"""

cell_values = {
    '0': -0.1,  # Empty space
    'P': -50,   # Pit
    'W': -100,  # Wumpus
    'G': 100,   # Gold
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
        # self.init_tab = init_tab
        self.position = None
        self.tab = init_tab
        self.size = (len(init_tab), len(init_tab[0]))
        self.__start_game()

    def __start_position(self):
        x = rd.randint(0, self.size[0]-1)
        y = rd.randint(0, self.size[1]-1)
        return x, y

    def __start_game(self):
        # self.tab = self.init_tab
        self.position = self.__start_position()

    def is_valid(self, position):
        if position[0] < 0 or position[0] >= self.size[0] or position[1] < 0 or position[1] >= self.size[1]:
            return False
        return True

    def sucessors(self, position):
        cds = [
            # (position[0], position[1]),
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
            return self.__start_position()

    def __mistake(self, position, action, mov='L'):
        k = 1 if(mov == 'L') else -1

        if action == 'UP':
            return position[0], position[1] - 1*k
        elif action == 'RIGHT':
            return position[0] - 1*k, position[1]
        elif action == 'DOWN':
            return position[0], position[1] + 1*k
        elif action == 'LEFT':
            return position[0] + 1*k, position[1]
        else:
            return position

    def transition_prob(self, position, action, next):
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

        if next == self.next(position, action):
            return 0.7
        elif next == self.__mistake(position, action, 'L'):
            return 0.2
        elif next == self.__mistake(position, action, 'R'):
            return 0.1

        return 0.0

    def reward(self, position, action):
        # if not self.is_valid(self.next(position, action)):
        #     return -1.0

        field = self.tab[position[0]][position[1]]
        return cell_values[field]

    def __str__(self):
        s = ''
        for i in range(4):
            for j in range(8):
                if i == self.position[0] and j == self.position[1]:
                    s += 'R '
                else:
                    s += self.tab[i][j] + ' '
            s += '\n'

        return s


if __name__ == '__main__':
    tab = Tabuleiro(board)
    print(tab)
