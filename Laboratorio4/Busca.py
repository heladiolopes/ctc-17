import numpy as np
from math import inf, fabs
from Tabuleiro import *

# actions = {'UP':0, 'DOWN':1, 'LEFT':2, 'RIGHT':3, 'START':4}


def value_iteration(tabuleiro, n_it = 10000, gamma = 0.98):
    sz = tabuleiro.size
    value = np.zeros(sz)

    for _ in range(n_it):
        new_value = np.zeros(sz)
        maxDif = -inf
        for i in range(sz[0]):
            for j in range(sz[1]):
                current = (i, j)

                actions = {'UP': 0, 'DOWN': 1, 'LEFT': 2, 'RIGHT': 3, 'START': 4}

                # if tabuleiro.tab[current[0]][current[1]] == '0':
                #     actions = {'UP': 0, 'DOWN': 1, 'LEFT': 2, 'RIGHT': 3}
                # else:
                #     actions = {'START': 0}

                value_k = np.zeros(len(actions))

                for action in actions.keys():
                    r = tabuleiro.reward(current, action)
                    for next in tabuleiro.sucessors(current):
                        transition_prob = tabuleiro.transition_prob(current, action, next)
                        value_k[actions[action]] += transition_prob * (r + gamma * value[next[0], next[1]])
                maxValue = max(value_k)
                maxDif = max(maxDif, fabs(maxValue - value[i, j]))
                new_value[i][j] = maxValue
        # print(new_value)
        value = new_value
        if maxDif < 1.0e-5:
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
            else:
                maxValue = -inf
                cell_text = ''
                for action in actions.keys():
                    next = tabuleiro.next(current, action)
                    if next in tabuleiro.sucessors(current) and value[next[0], next[1]] > maxValue:
                        maxValue = value[next[0], next[1]]
                        cell_text = action
            print('{:5} '.format(cell_text), end='')
            if j < sz[1] - 1:
                print(',', end='')
        print(']')


def print_values(value):
    for i in range(len(value)):
        for j in range(len(value[i])):
            print('{:10.4f}'.format(value[i][j]), end=' ')
        print('')


if __name__ == '__main__':
    world = Tabuleiro(board)
    value = value_iteration(world)
    print_values(value)
    best_policy(world, value)