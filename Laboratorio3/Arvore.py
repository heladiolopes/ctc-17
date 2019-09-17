import copy
import statistics


class Node:
    def __init__(self, teste):
        self.filhos = []
        self.teste = teste


def Maioria(exemplos):
    return statistics.mode(exemplos[-1])


def escolher_atributo(atributos, exemplos):
    return 0


def Aprendizado(exemplos, atributos, padrao):
    diff = False
    elemento = exemplos[0][-1]
    for linha in exemplos:
        if linha[-1] != elemento:
            diff = True

    if len(exemplos) == 0:
        return padrao
    elif diff:
        return elemento
    elif len(atributos) == 0:
        return Maioria(exemplos)
    else:
        melhor = escolher_atributo(atributos, exemplos)
        arvore = Node(melhor)
        for valor in atributos[melhor]:

            exemplos_i = []
            for l in exemplos:
                if l[melhor] == valor:
                    lista = copy.deepcopy(l)
                    exemplos_i.append(lista.pop(melhor))

            atributos_i = {}
            for k in atributos.keys():
                if k < melhor:
                    atributos_i[k] = atributos[k]
                elif k > melhor:
                    atributos_i[k-1] = atributos[k]

            sub_arvore = Aprendizado(exemplos_i, atributos_i, Maioria(exemplos))
            arvore.filhos.append((valor, sub_arvore))

    return arvore
