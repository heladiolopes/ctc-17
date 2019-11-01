import numpy as np
from math import inf, fabs
from Tabuleiro import *

# actions = {'UP':0, 'DOWN':1, 'LEFT':2, 'RIGHT':3, 'START':4}


def value_iteration(tabuleiro, n_it=3, gamma=1):
    sz = tabuleiro.size
    value = np.zeros(sz)

    for _ in range(n_it):
        new_value = np.zeros(sz)

        for i in range(sz[0]):
            for j in range(sz[1]):
                current = (i, j)

                actions = {'UP': 0, 'DOWN': 1, 'LEFT': 2, 'RIGHT': 3, 'START': 4}

                r = tabuleiro.reward(current)

                value_k = np.zeros(len(actions))

                # Equação de bellman
                for action in actions.keys():
                    for next in tabuleiro.sucessors(current):
                        transition_prob = tabuleiro.transition_prob(current, action, next)
                        value_k[actions[action]] += transition_prob * value[next[0], next[1]]

                maxValue = max(value_k)
                new_value[i][j] = r + gamma * maxValue

        maxDif = -inf
        for i in range(sz[0]):
            for j in range(sz[1]):
                maxDif = max(maxDif, fabs(value[i,j] - new_value[i, j]))
        value = new_value

        if maxDif < 5:
            break

    return value


def best_policy(tabuleiro, value):
    sz = tabuleiro.size
    actions = {'UP':0, 'DOWN':1, 'LEFT':2, 'RIGHT':3, 'START':4}

    for i in range(sz[0]):
        print('[', end='')
        for j in range(sz[1]):
            current = (i, j)
            if tabuleiro.tab[i][j] != '0':
                cell_text = 'START'
                if tabuleiro.tab[i][j] == 'W':
                    cell_text = 'Wumpus'
                elif tabuleiro.tab[i][j] == 'G':
                    cell_text = 'Gold'
                else:
                    cell_text = 'Pit'
            else:
                maxValue = -inf
                cell_text = ''
                for action in actions.keys():
                    next = tabuleiro.next(current, action)
                    if next in tabuleiro.sucessors(current) and value[next[0], next[1]] > maxValue:
                        maxValue = value[next[0], next[1]]
                        cell_text = action
            cell_text = cell_text.center(9)
            print(cell_text, end='')
            if j < sz[1] - 1:
                print(',', end='')
        print(']\n')


def print_values(value):
    for i in range(len(value)):
        for j in range(len(value[i])):
            print('{:8.2f}'.format(value[i][j]), end=' ')
        print('\n')
    print('--------------------------------------------------------------')


if __name__ == '__main__':
    world = Tabuleiro(board)
    value = value_iteration(world)
    print('')
    print_values(value)
    print('')
    best_policy(world, value)