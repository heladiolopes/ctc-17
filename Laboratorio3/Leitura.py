def Leitura(file, sep):
    f = open(file, 'r')
    lines = f.readlines()

    exemplos = []

    for l in lines:
        exemplos.append(l[:-1].split(sep))

    return exemplos


if __name__ == '__main__':
    exemplos = Leitura('ml-1m/ratings.dat', '::')
    for l in exemplos:
        print(l)
