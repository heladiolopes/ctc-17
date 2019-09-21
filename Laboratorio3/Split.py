import random
from Leitura import Atributos_Exemplos


def split_train_test(examples, percent):
    n = len(examples)

    random.shuffle(examples)

    train = examples[:int(percent*n)]
    test = examples[int(percent*n):]

    return train, test


if __name__ == '__main__':
    # attributes = {0: ["Ensolarado", "Nublado", "Chuvoso"], 1: ["Quente", "Boa", "Fria"],
    #               2: ["Alta", "Normal"], 3: ["Forte", "Fraco"]}
    #
    # examples = [["Ensolarado", "Quente", "Alta", "Fraco", "NAO"],
    #             ["Ensolarado", "Quente", "Alta", "Forte", "NAO"],
    #             ["Nublado", "Quente", "Alta", "Fraco", "SIM"],
    #             ["Chuvoso", "Boa", "Alta", "Fraco", "SIM"],
    #             ["Chuvoso", "Fria", "Normal", "Fraco", "SIM"],
    #             ["Chuvoso", "Fria", "Normal", "Forte", "NAO"],
    #             ["Nublado", "Fria", "Normal", "Forte", "SIM"],
    #             ["Ensolarado", "Boa", "Alta", "Fraco", "NAO"],
    #             ["Ensolarado", "Fria", "Normal", "Fraco", "SIM"],
    #             ["Chuvoso", "Boa", "Normal", "Fraco", "SIM"],
    #             ["Ensolarado", "Boa", "Normal", "Forte", "SIM"],
    #             ["Nublado", "Boa", "Alta", "Forte", "SIM"],
    #             ["Nublado", "Quente", "Normal", "Fraco", "SIM"],
    #             ["Chuvoso", "Boa", "Alta", "Forte", "NAO"]]
    examples, attributes = Atributos_Exemplos()

    print('Comeco')
    tr, ts = split_train_test(examples, 0.7)
    print('FIM')


