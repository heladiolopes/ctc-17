from Arvore import Aprendizado, Maioria, MostraArvore, Classificar
from Leitura import Atributos_Exemplos
from datetime import datetime as dt
import os
from Split import split_train_test

t = dt.now()
# attributes = {0: ["Ensolarado", "Nublado", "Chuvoso"], 1: ["Quente", "Boa", "Fria"],
#               2: ["Alta", "Normal"], 3: ["Forte", "Fraco"]}
#
# examples = [["Ensolarado", "Quente", "Alta", "Fraco", "NAO"],
#                 ["Ensolarado", "Quente", "Alta", "Forte", "NAO"],
#                 ["Nublado", "Quente", "Alta", "Fraco", "SIM"],
#                 ["Chuvoso", "Boa", "Alta", "Fraco", "SIM"],
#                 ["Chuvoso", "Fria", "Normal", "Fraco", "SIM"],
#                 ["Chuvoso", "Fria", "Normal", "Forte", "NAO"],
#                 ["Nublado", "Fria", "Normal", "Forte", "SIM"],
#                 ["Ensolarado", "Boa", "Alta", "Fraco", "NAO"],
#                 ["Ensolarado", "Fria", "Normal", "Fraco", "SIM"],
#                 ["Chuvoso", "Boa", "Normal", "Fraco", "SIM"],
#                 ["Ensolarado", "Boa", "Normal", "Forte", "SIM"],
#                 ["Nublado", "Boa", "Alta", "Forte", "SIM"],
#                 ["Nublado", "Quente", "Normal", "Fraco", "SIM"],
#                 ["Chuvoso", "Boa", "Alta", "Forte", "NAO"]]
examples, attributes = Atributos_Exemplos()
print(dt.now() - t)

# t = dt.now()
# arvore = Aprendizado(examples, attributes, Maioria(examples))
# print(dt.now() - t)

# MostraArvore(arvore)

"""
Segmentar dados
"""
train, test = split_train_test(examples, 0.6)
print('Dividido')

t = dt.now()
arvore = Aprendizado(train, attributes, Maioria(train))
print(dt.now() - t)

result = []
for line in test:
    result.append(Classificar(arvore, line))

acerto = 0
for i in range(len(test)):
    print('ESPERADO: {:5} | OBTIDO: {:5}'.format(test[i][-1], result[i]))
    if result[i] == test[i][-1]:
        acerto += 1

print(acerto/len(result))


os.system('play -nq -t alsa synth {} sine {}'.format(0.3, 440))
# print(Classificar(arvore, ["Ensolarado", "Fria", "Alta", "Forte"]))
