from math import log, inf
from collections import defaultdict
from Leitura import Atributos_Exemplos

# atributos -> dicionário: chave é o índice de exemplos e o valor corresponde a uma lista de valores possíveis
# exemplos -> matriz: cada linha corresponde a um exemplo (com atributos e padrão)


def examples_with_attribute(examples, attribute, attribute_value):
    new_examples = []

    for i in range(len(examples)):
        if attribute_value == examples[i][attribute]:
            new_examples.append(examples[i])

    return new_examples


def initial_entropy(examples):
    freq = defaultdict(int)

    sum_freq = 0
    for i in range(len(examples)):
        freq[examples[i][-1]] += 1
        sum_freq += 1

    sum_freq = float(sum_freq)
    entropy = 0.0
    for attribute_value in freq:
        entropy += (-freq[attribute_value])*(log(freq[attribute_value]/sum_freq, 2))/sum_freq

    #print(freq)
    #print(entropy)

    return entropy


def choose_attribute(attributes, examples):
    examples_size = len(examples)
    e = initial_entropy(examples)

    best_gain = -inf
    best_gain_index = -1
    for attribute in attributes:
        gain = e
        for attribute_value in attributes[attribute]:
            new_examples = examples_with_attribute(examples, attribute, attribute_value)
            attribute_value_size = len(new_examples)
            attribute_value_entropy = initial_entropy(new_examples)
            gain -= (float(attribute_value_size)/float(examples_size))*attribute_value_entropy
        if gain > best_gain:
            best_gain = gain
            best_gain_index = attribute
        #print(attribute, gain)

    return best_gain_index


if __name__ == "__main__":
    """
    attributes = {0: ["Ensolarado", "Nublado", "Chuvoso"], 1: ["Quente", "Boa", "Fria"],
                  2: ["Alta", "Normal"], 3: ["Forte", "Fraco"]}
    examples = [["Ensolarado", "Quente", "Alta", "Fraco", "NAO"],
                ["Ensolarado", "Quente", "Alta", "Forte", "NAO"],
                ["Nublado", "Quente", "Alta", "Fraco", "SIM"],
                ["Chuvoso", "Boa", "Alta", "Fraco", "SIM"],
                ["Chuvoso", "Fria", "Normal", "Fraco", "SIM"],
                ["Chuvoso", "Fria", "Normal", "Forte", "NAO"],
                ["Nublado", "Fria", "Normal", "Forte", "SIM"],
                ["Ensolarado", "Boa", "Alta", "Fraco", "NAO"],
                ["Ensolarado", "Fria", "Normal", "Fraco", "SIM"],
                ["Chuvoso", "Boa", "Normal", "Fraco", "SIM"],
                ["Ensolarado", "Boa", "Normal", "Forte", "SIM"],
                ["Nublado", "Boa", "Alta", "Forte", "SIM"],
                ["Nublado", "Quente", "Normal", "Fraco", "SIM"],
                ["Chuvoso", "Boa", "Alta", "Forte", "NAO"]]
    """

    examples, attributes = Atributos_Exemplos()

    _ = choose_attribute(attributes, examples)

