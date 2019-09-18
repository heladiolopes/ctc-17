import copy
import statistics
from scipy import stats as s
from Escolher_Atributo import choose_attribute


class Node:
    def __init__(self, teste):
        self.filhos = []
        self.teste = teste


def Maioria(exemplos):
    l = []
    for i in exemplos:
        l.append(i[-1])
    # print(l)
    # return statistics.mode(l)
    mode = int(s.mode(l)[0])
    # print(mode)
    return mode


def Aprendizado(exemplos, atributos, padrao):
    diff = False
    elemento = None
    if len(exemplos) > 0:
        elemento = exemplos[0][-1]
        for linha in exemplos:
            if linha[-1] != elemento:
                diff = True

    if len(exemplos) == 0:
        # print('{:10} ->'.format('PADRÂO'), padrao)
        return Node(padrao)
    elif not diff:
        print('{:10} ->'.format('ELEMENTO'), elemento)
        return Node(elemento)
    elif len(atributos) == 0:
        x = Maioria(exemplos)
        print('{:10} ->'.format('MAIORIA'), x)
        return Node(x)
    else:
        melhor = choose_attribute(atributos, exemplos)
        print('{:10} ->'.format('MELHOR'), melhor)
        if melhor == -1:
            melhor = list(atributos.keys())[0]
            print('{:10} ->'.format('CORRIGIDO'), melhor, atributos[melhor])

        arvore = Node(melhor)
        m = Maioria(exemplos)
        for valor in atributos[melhor]:

            exemplos_i = []
            for l in exemplos:
                if l[melhor] == valor:
                    exemplos_i.append(l)

            atributos_i = copy.deepcopy(atributos)
            atributos_i.pop(melhor)

            sub_arvore = Aprendizado(exemplos_i, atributos_i, m)
            arvore.filhos.append((valor, sub_arvore))

        return arvore


def tab(n):
    s = ''
    for i in range(n):
        s += '\t'
    return s


def MostraArvore(node, n=0):
    print(tab(n), '(', node.teste, sep='', end='')
    for f in node.filhos:
        print('\n', tab(n+1), f[0], '')
        MostraArvore(f[1], n+1)
    if len(node.filhos) == 0:
        print(')')
    else:
        print(tab(n), ')')


def Classificar(node, elemento):

    if len(node.filhos) == 0:
        return node.teste

    else:
        for f in node.filhos:
            if elemento[node.teste] == f[0]:
                return Classificar(f[1], elemento)
