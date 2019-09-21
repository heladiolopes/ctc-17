from Arvore import Aprendizado, Maioria, Classificar
from Leitura import Atributos_Exemplos
from Split import split_train_test
from A_Priori import *
from Analise_Comparativa import Analise

# Arvore de classificação
examples, attributes = Atributos_Exemplos()
train, test = split_train_test(examples, 0.6)
arvore = Aprendizado(train, attributes, Maioria(train))

predito_arvore = []
correto_arvore = []
for line in test:
    predito_arvore.append(int(Classificar(arvore, line)))
    correto_arvore.append(int(line[-1]))

analise_arvore = Analise(correto_arvore, predito_arvore, 5)
analise_arvore.estatisticas()

# A priori
examples = a_priori_examples()
train, test = a_priori_train_test(examples)
moviesRatingsDict, all_ratings = a_priori_median_ratings(train)
test_rating = a_priori_rating(test, moviesRatingsDict, all_ratings)

predito_priori = []
correto_priori = []
for i in range(len(test)):
    predito_priori.append(int(test[i][1]))
    correto_priori.append(int(test_rating[i][1]))

analise_arvore = Analise(correto_priori, predito_priori, 5)
analise_arvore.estatisticas()
