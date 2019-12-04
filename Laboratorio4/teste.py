import numpy as np
import matplotlib.pyplot as plt


init_tab = [
    ['0', 'P', '0', '0', '0', '0', 'P', '0'],
    ['W', 'G', 'P', '0', '0', '0', 'P', '0'],
    ['0', '0', '0', '0', 'W', 'G', 'R', '0'],
    ['0', '0', 'P', '0', '0', '0', 'P', '0'],
]
# init_tab = [
#     [0, 10, 0, 0, 0, 0, 10, 0],
#     [2, 5, 10, 0, 0, 0, 10, 0],
#     [0, 0, 0, 0, 2, 5, 0, 0],
#     [0, 0, 10, 0, 0, 0, 10, 0],
# ]

convert = {
    '0': 100,
    'P': 0,
    'W': 30,
    'G': 60,
    'R': 90,
}


def print_maze(tab, name):

    t = []
    for i in range(len(tab)):
        t.append([])
        for k in range(len(tab[i])):
            t[i].append(convert[tab[i][k]])

    t = np.array(t)

    plt.grid('on')
    nrows, ncols = len(tab), len(tab[0])
    ax = plt.gca()
    ax.set_xticks(np.arange(0.5, nrows, 1))
    ax.set_yticks(np.arange(0.5, ncols, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    canvas = np.copy(t)

    img = plt.imshow(canvas, interpolation='none', cmap='gray')
    # plt.show()
    plt.savefig(name+'.png')
    return img

if __name__ == '__main__':
    print_maze(init_tab)