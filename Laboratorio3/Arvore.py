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
                    lista = copy.deepcopy(l)
                    lista.pop(melhor)
                    exemplos_i.append(lista)

            atributos_i = {}
            for k in atributos:
                if k < melhor:
                    atributos_i[k] = atributos[k]
                elif k > melhor:
                    atributos_i[k-1] = atributos[k]

            sub_arvore = Aprendizado(exemplos_i, atributos_i, m)
            arvore.filhos.append((valor, sub_arvore))

        return arvore


def MostraArvore(node):
    print('(', node.teste, end='')
    for f in node.filhos:
        print(f[0], end='')
        MostraArvore(f[1])
    print(')',end='')
