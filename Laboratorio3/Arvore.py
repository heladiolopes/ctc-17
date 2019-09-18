import copy
import statistics
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
    return statistics.mode(l)


def Aprendizado(exemplos, atributos, padrao):
    diff = False
    elemento = exemplos[0][-1]
    for linha in exemplos:
        if linha[-1] != elemento:
            diff = True

    if len(exemplos) == 0:
        return Node(padrao)
    elif not diff:
        return Node(elemento)
    elif len(atributos) == 0:
        return Maioria(exemplos)
    else:
        melhor = choose_attribute(atributos, exemplos)
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
    print(tab(n), '(', node.teste, sep='')
    for f in node.filhos:
        print(tab(n+1), f[0], '')
        MostraArvore(f[1], n+1)
    print(tab(n), ')')


def Classificar(node, elemento):

    if len(node.filhos) == 0:
        return node.teste

    else:
        for f in node.filhos:
            if elemento[node.teste] == f[0]:
                return Classificar(f[1], elemento)
